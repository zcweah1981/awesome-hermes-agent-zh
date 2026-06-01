#!/usr/bin/env python3
"""Official-source sync helper for the Hermes Chinese content repo.

This script is intentionally local-first and side-effect safe:
- `check` validates registry/policy contracts and can optionally check source reachability.
- `digest` renders a concise Markdown digest for maintainers.
- `plan` reads the version ledger and official release info to suggest sync steps.
- `issue --dry-run` renders a GitHub issue body without calling GitHub.

No credentials are read or printed.
"""
from __future__ import annotations

import argparse
import json
import sys
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - PyYAML is available in this repo environment.
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = REPO_ROOT / "governance" / "upstream-source-registry.yaml"
DEFAULT_LEDGER = REPO_ROOT / "governance" / "version-ledger.yaml"
DEFAULT_POLICY = REPO_ROOT / "governance" / "upstream-sync-policy.md"
DEFAULT_HUMAN_REGISTRY = REPO_ROOT / "governance" / "upstream-source-registry.md"

REQUIRED_SOURCE_FIELDS = ("id", "tier", "name", "url")
FORBIDDEN_PUBLIC_TERMS = ("dispatch", "worker_run", "runtime log", "private tokens", "raw credentials")

@dataclass(frozen=True)
class CheckOptions:
    registry: Path
    ledger: Path
    policy: Path
    human_registry: Path
    no_network: bool

def fetch_latest_github_release(repo: str = "NousResearch/hermes-agent") -> dict[str, Any] | None:
    try:
        req = Request(
            f"https://api.github.com/repos/{repo}/releases/latest",
            headers={"User-Agent": "hermes-zh-upstream-sync", "Accept": "application/vnd.github.v3+json"}
        )
        with urlopen(req, timeout=5) as res:
            data = json.loads(res.read().decode("utf-8"))
            return {
                "tag_name": data.get("tag_name"),
                "html_url": data.get("html_url"),
                "body": data.get("body", ""),
                "published_at": data.get("published_at")
            }
    except Exception:
        return None

def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)

def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"YAML file not found: {path}")
    if yaml is None:
        raise RuntimeError("PyYAML is required to parse YAML files")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"YAML root must be a mapping: {path}")
    return data

def source_list(registry: dict[str, Any]) -> list[dict[str, Any]]:
    sources = registry.get("sources")
    if not isinstance(sources, list):
        return []
    return [source for source in sources if isinstance(source, dict)]

def check_url(url: str, timeout: float = 8.0) -> dict[str, Any]:
    request = Request(url, method="HEAD", headers={"User-Agent": "hermes-zh-upstream-sync-check/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return {"status": "ok", "code": response.status}
    except HTTPError as exc:
        if exc.code in {403, 405}:
            return {"status": "warning", "code": exc.code, "message": "HEAD not allowed or blocked"}
        return {"status": "failed", "code": exc.code, "message": str(exc)}
    except URLError as exc:
        return {"status": "failed", "message": str(exc.reason)}
    except Exception as exc:
        return {"status": "failed", "message": str(exc)}

def categorize_changes(body: str) -> list[str]:
    categories = []
    lower_body = body.lower()
    keywords = {
        "install": ["install", "npm", "pip", "setup"],
        "cli": ["cli", "command", "args", "terminal"],
        "configuration": ["config", ".env", "yaml", "settings"],
        "provider": ["openai", "anthropic", "gemini", "provider", "model"],
        "tools": ["tool", "function call"],
        "skills": ["skill"],
        "mcp": ["mcp", "context protocol"],
        "breaking_change": ["breaking", "deprecated", "removed"],
        "bug_fix": ["fix", "bug", "resolved"],
        "new_feature": ["new", "added", "feature"]
    }
    for cat, words in keywords.items():
        if any(word in lower_body for word in words):
            categories.append(cat)
    return sorted(list(set(categories)))

def validate(options: CheckOptions) -> dict[str, Any]:
    issues: list[str] = []
    warnings: list[str] = []
    required_files = {
        repo_relative(options.registry): "ok" if options.registry.exists() else "missing",
        repo_relative(options.ledger): "ok" if options.ledger.exists() else "missing",
        repo_relative(options.policy): "ok" if options.policy.exists() else "missing",
        repo_relative(options.human_registry): "ok" if options.human_registry.exists() else "missing",
    }
    for rel, status in required_files.items():
        if status != "ok":
            issues.append(f"required file missing: {rel}")

    registry: dict[str, Any] = {}
    sources: list[dict[str, Any]] = []
    if options.registry.exists():
        try:
            registry = load_yaml(options.registry)
            sources = source_list(registry)
        except Exception as exc:
            issues.append(f"registry parse failed: {exc}")

    ledger: dict[str, Any] = {}
    if options.ledger.exists():
        try:
            ledger = load_yaml(options.ledger)
            if ledger.get("ledger_meta", {}).get("project_id") != "hermes-zh":
                issues.append(f"ledger project_id mismatch: expected hermes-zh, got {ledger.get('ledger_meta', {}).get('project_id')}")
        except Exception as exc:
            issues.append(f"ledger parse failed: {exc}")

    if not sources:
        issues.append("registry must contain a sources list")

    source_ids: list[str] = []
    duplicate_ids: set[str] = set()
    seen_ids: set[str] = set()
    official_count = 0
    provider_count = 0
    local_count = 0
    reachability: dict[str, Any] = {}

    for source in sources:
        source_id = str(source.get("id", ""))
        if source_id:
            source_ids.append(source_id)
            if source_id in seen_ids:
                duplicate_ids.add(source_id)
            seen_ids.add(source_id)

        missing = [field for field in REQUIRED_SOURCE_FIELDS if not source.get(field)]
        if missing:
            issues.append(f"source {source_id or '<missing-id>'} missing fields: {', '.join(missing)}")

        tier = source.get("tier")
        if tier == "official":
            official_count += 1
        elif tier == "provider_official":
            provider_count += 1
        elif tier == "local_content":
            local_count += 1

        url = source.get("url")
        if isinstance(url, str) and url.startswith("http") and not options.no_network:
            reachability[source_id or url] = check_url(url)

    if duplicate_ids:
        issues.append(f"duplicate source ids: {', '.join(sorted(duplicate_ids))}")
    if official_count < 2:
        issues.append("registry must include at least two official sources: official docs and official GitHub")
    if "hermes-official-docs" not in source_ids:
        issues.append("registry missing official source id: hermes-official-docs")
    if "hermes-official-github" not in source_ids:
        issues.append("registry missing official source id: hermes-official-github")
    if "content-repo" not in source_ids:
        issues.append("registry missing local content source id: content-repo")

    source_tiers = registry.get("source_tiers", {}) if registry else {}
    official_tier = source_tiers.get("official", {}) if isinstance(source_tiers, dict) else {}
    if official_tier.get("required_before_public_claim") is not True:
        issues.append("official tier must set required_before_public_claim: true")

    if options.policy.exists():
        policy_text = options.policy.read_text(encoding="utf-8")
        for required_phrase in ("来源优先级", "同步流程", "禁止项", "R1", "R2"):
            if required_phrase not in policy_text:
                issues.append(f"policy missing required section/phrase: {required_phrase}")
        if "API Key" not in policy_text and "Token" not in policy_text:
            warnings.append("policy should explicitly mention credential/token prohibition")

    failed_reachability = [key for key, value in reachability.items() if value.get("status") == "failed"]
    for key in failed_reachability:
        warnings.append(f"source reachability failed: {key}")

    # Version Info
    baseline_ver = ledger.get("current_content_baseline") or registry.get('hermes_upstream_baseline_version', 'unknown')
    latest_release = fetch_latest_github_release() if not options.no_network else None
    latest_ver = latest_release.get("tag_name") if latest_release else None
    
    change_cats = categorize_changes(latest_release.get("body", "")) if latest_release else []
    affected_docs_candidates = []
    if change_cats and ledger.get("sync_priority_tiers"):
        tiers = ledger.get("sync_priority_tiers")
        for tier_name, tier_info in tiers.items():
            tier_cats = tier_info.get("categories", [])
            if any(c in tier_cats for c in change_cats):
                affected_docs_candidates.extend(tier_info.get("affected_docs", []))
    
    version_info = {
        'baseline': baseline_ver,
        'latest': latest_ver,
        'html_url': latest_release.get("html_url") if latest_release else None,
        'outdated': False,
        'status': 'unknown' if latest_ver is None else 'up_to_date',
        'change_categories': change_cats,
        'affected_docs_candidates': sorted(list(set(affected_docs_candidates)))
    }
    if latest_ver and baseline_ver and latest_ver != baseline_ver:
        version_info['outdated'] = True
        version_info['status'] = 'sync_needed'
        warnings.append(f"Official upstream release is at {latest_ver}, but baseline is {baseline_ver}")

    payload = {
        "status": "failed" if issues else "ok",
        "checked_at": date.today().isoformat(),
        "network_checked": not options.no_network,
        "required_files": required_files,
        "source_ids": source_ids,
        "version_sync": version_info,
        "summary": {
            "sources_total": len(sources),
            "official_sources": official_count,
            "provider_official_sources": provider_count,
            "local_content_sources": local_count,
        },
        "issues": issues,
        "warnings": warnings,
        "reachability": reachability,
    }
    return payload

def render_check_markdown(payload: dict[str, Any]) -> str:
    lines = ["# 官方来源同步 Check", "", f"- status: `{payload['status']}`", f"- checked_at: `{payload['checked_at']}`", f"- network_checked: `{str(payload['network_checked']).lower()}`", ""]
    lines.append("## Version Status")
    v = payload["version_sync"]
    lines.append(f"- Baseline: `{v['baseline']}`")
    lines.append(f"- Latest: `{v['latest'] or 'unknown'}`")
    lines.append(f"- Outdated: `{str(v['outdated']).lower()}`")
    if v['html_url']:
        lines.append(f"- Release URL: {v['html_url']}")
    if v['change_categories']:
        lines.append(f"- Categories: {', '.join(v['change_categories'])}")
    if v.get('affected_docs_candidates'):
        lines.append("- Affected Docs (Candidates):")
        lines.extend(f"  - {doc}" for doc in v['affected_docs_candidates'])
    lines.append("")
    lines.append("## Summary")
    for key, value in payload["summary"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Issues")
    if payload["issues"]:
        lines.extend(f"- {issue}" for issue in payload["issues"])
    else:
        lines.append("- none")
    lines.append("")
    return "\n".join(lines)

def render_digest(options: CheckOptions) -> str:
    registry = load_yaml(options.registry)
    payload = validate(options)
    sources = source_list(registry)

    lines = [
        "# 官方来源同步 Digest",
        "",
        f"生成日期：{date.today().isoformat()}",
        "",
        "## 版本台账摘要",
        "",
        f"- 当前基线: `{payload['version_sync']['baseline']}`",
        f"- 官方最新: `{payload['version_sync']['latest'] or 'unknown'}`",
        f"- 状态: `{'⚠️ 落后' if payload['version_sync']['outdated'] else '✅ 已对齐'}`",
        "",
        "## 已登记来源",
        "",
        "| ID | Tier | Name | URL | Rule |",
        "|---|---|---|---|---|",
    ]
    for source in sources:
        lines.append(
            "| `{id}` | `{tier}` | {name} | <{url}> | {rule} |".format(
                id=source.get("id", ""),
                tier=source.get("tier", ""),
                name=str(source.get("name", "")).replace("|", "/"),
                url=source.get("url", ""),
                rule=str(source.get("sync_rule", "")).replace("|", "/"),
            )
        )
    lines.extend([
        "",
        "## 禁止项确认",
        "",
        "- 不写入 API Key、Token、cookie、session。",
        "- 不把站点运行机制当作 Hermes 产品能力。",
        "- 不把二手文章直接变成正式教程结论。",
        "",
    ])
    digest = "\n".join(lines)
    for term in FORBIDDEN_PUBLIC_TERMS[:2]:
        digest = digest.replace(term, "[internal-term-redacted]")
    return digest

def render_plan(options: CheckOptions) -> dict[str, Any]:
    payload = validate(options)
    v = payload["version_sync"]
    
    plan_data = {
        "status": "up_to_date" if not v["outdated"] else "sync_needed",
        "baseline": v["baseline"],
        "latest": v["latest"],
        "outdated": v["outdated"],
        "steps": []
    }

    if v["outdated"]:
        plan_data["steps"] = [
            f"1. 复查官方 Release Notes: {v['html_url']}",
            f"2. 识别变更分类: {', '.join(v['change_categories'])}",
            "3. 确定受影响的文档列表 (参考 governance/version-ledger.yaml 中的 P0/P1/P2 定义)",
            f"4. 在内容仓执行同步，更新 baseline 为 {v['latest']}",
            "5. 更新 governance/version-ledger.yaml 的 versions 列表"
        ]
    else:
        plan_data["steps"] = ["无需同步。当前内容仓已与上游基线对齐。"]

    return plan_data

def write_or_print(text: str, output: str | None) -> None:
    if output:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path}")
    else:
        print(text)

def add_common_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--policy", type=Path, default=DEFAULT_POLICY)
    parser.add_argument("--human-registry", type=Path, default=DEFAULT_HUMAN_REGISTRY)
    parser.add_argument("--no-network", action="store_true", help="Skip reachability checks")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Official-source sync helper")
    add_common_options(parser)
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="Validate registry, ledger and policy")
    add_common_options(check)
    check.add_argument("--format", choices=("markdown", "json"), default="markdown")
    check.add_argument("--output")

    digest = sub.add_parser("digest", help="Render Markdown digest")
    add_common_options(digest)
    digest.add_argument("--output")

    plan = sub.add_parser("plan", help="Generate sync plan based on ledger and latest release")
    add_common_options(plan)
    plan.add_argument("--format", choices=("markdown", "json"), default="markdown")
    plan.add_argument("--output")

    issue = sub.add_parser("issue", help="Render issue body; only dry-run is supported")
    add_common_options(issue)
    issue.add_argument("--dry-run", action="store_true", help="Deprecated, no-op")
    issue.add_argument("--format", choices=("markdown", "json"), default="markdown")
    issue.add_argument("--output")
    return parser

def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    options = CheckOptions(args.registry, args.ledger, args.policy, args.human_registry, args.no_network)

    if args.command == "check":
        payload = validate(options)
        text = json.dumps(payload, ensure_ascii=False, indent=2) if args.format == "json" else render_check_markdown(payload)
        write_or_print(text, args.output)
        return 0 if payload["status"] == "ok" else 1

    if args.command == "digest":
        write_or_print(render_digest(options), args.output)
        return 0

    if args.command == "plan":
        plan_data = render_plan(options)
        if args.format == "json":
            text = json.dumps(plan_data, ensure_ascii=False, indent=2)
        else:
            lines = [f"# Sync Plan for {plan_data['latest'] or plan_data['baseline']}", "", f"Status: {plan_data['status']}"]
            lines.append(f"Outdated: {str(plan_data['outdated']).lower()}")
            lines.append("")
            lines.append("## Steps")
            lines.extend(plan_data["steps"])
            text = "\n".join(lines)
        write_or_print(text, args.output)
        return 0

    if args.command == "issue":
        payload = validate(options)
        v = payload.get("version_sync", {})
        baseline = v.get("baseline", "unknown")
        latest = v.get("latest", "unknown")
        outdated = v.get("outdated", False)
        
        digest = render_digest(options)
        title = "R1 官方来源同步：R2 官方来源确认待办"
        warning = ""
        affected_section = ""
        if v.get('affected_docs_candidates'):
            affected_section = "\n## 影响页面候选\n\n" + "\n".join(f"- {doc}" for doc in v['affected_docs_candidates']) + "\n"

        if outdated:
            title = f"⚠️ [需要同步] Hermes 官方版本已更新到 {latest}，本地基线停留在 {baseline}"
            warning = f"## ⚠️ 版本落后警告\n\nHermes 官方最新 Release 是 `{latest}`，但内容仓当前登记的基线版本是 `{baseline}`。\n\n请内容维护者复查官方 release notes，如果存在破坏性变更、新功能或废弃项，请启动同步工作流。\n\n---\n\n"

        body = f"{warning}## 背景\nR1 已建立官方来源 registry / policy；R2 已确认国内模型与部署页面的厂商官方来源。\n\n## R2 digest\n\n{digest}\n{affected_section}\n## 建议处理\n\n- [ ] 后续修改国内模型页面前，先复查 registry 中对应 source_urls。\n- [ ] 对任何影响用户操作的正文改动记录 source / checked_at / affected_docs。\n\n"
        
        if args.dry_run:
            body += "## Dry-run 声明\n本输出仅用于本地 dry-run；未调用 GitHub API，未创建远端 issue。"

        if args.format == "json":
            text = json.dumps({"dry_run": args.dry_run, "title": title, "body": body, "outdated": outdated}, ensure_ascii=False, indent=2)
        else:
            text = f"# {title}\n\ndry_run: {str(args.dry_run).lower()}\n\n{body}"
        write_or_print(text, args.output)
        return 0

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
