#!/usr/bin/env python3
"""Official-source sync helper for the Hermes Chinese content repo.

This script is intentionally local-first and side-effect safe:
- `check` validates registry/policy contracts and can optionally check source reachability.
- `digest` renders a concise Markdown digest for maintainers.
- `issue --dry-run` renders a GitHub issue body without calling GitHub.

No credentials are read or printed.
"""
from __future__ import annotations

import argparse
import json
import sys
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
DEFAULT_POLICY = REPO_ROOT / "governance" / "upstream-sync-policy.md"
DEFAULT_HUMAN_REGISTRY = REPO_ROOT / "governance" / "upstream-source-registry.md"

REQUIRED_SOURCE_FIELDS = ("id", "tier", "name", "url")
FORBIDDEN_PUBLIC_TERMS = ("dispatch", "worker_run", "runtime log", "private tokens", "raw credentials")


@dataclass(frozen=True)
class CheckOptions:
    registry: Path
    policy: Path
    human_registry: Path
    no_network: bool


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def load_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"registry not found: {path}")
    if yaml is None:
        raise RuntimeError("PyYAML is required to parse upstream-source-registry.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("registry YAML root must be a mapping")
    return data


def source_list(registry: dict[str, Any]) -> list[dict[str, Any]]:
    sources = registry.get("sources")
    if not isinstance(sources, list):
        return []
    return [source for source in sources if isinstance(source, dict)]


def check_url(url: str, timeout: float = 8.0) -> dict[str, Any]:
    request = Request(url, method="HEAD", headers={"User-Agent": "hermes-zh-upstream-sync-check/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:  # nosec: official registry URLs only, operator-controlled.
            return {"status": "ok", "code": response.status}
    except HTTPError as exc:
        # Some hosts disallow HEAD but still exist. Report HTTP code without treating 405/403 as hard crash.
        if exc.code in {403, 405}:
            return {"status": "warning", "code": exc.code, "message": "HEAD not allowed or blocked"}
        return {"status": "failed", "code": exc.code, "message": str(exc)}
    except URLError as exc:
        return {"status": "failed", "message": str(exc.reason)}
    except Exception as exc:  # pragma: no cover - defensive, reported in JSON.
        return {"status": "failed", "message": str(exc)}


def validate(options: CheckOptions) -> dict[str, Any]:
    issues: list[str] = []
    warnings: list[str] = []
    required_files = {
        repo_relative(options.registry): "ok" if options.registry.exists() else "missing",
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
            registry = load_registry(options.registry)
            sources = source_list(registry)
        except Exception as exc:
            issues.append(f"registry parse failed: {exc}")

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

    r2_provider_block = registry.get("provider_sources_to_fill_in_r2", {})
    r2_providers = r2_provider_block.get("providers", []) if isinstance(r2_provider_block, dict) else []
    r2_confirmed = sum(
        1
        for provider in r2_providers
        if str(provider.get("status", "")).startswith("confirmed_") and provider.get("source_urls")
    )
    r2_pending = sum(
        1
        for provider in r2_providers
        if str(provider.get("status", "")).startswith("needs_") or not provider.get("source_urls")
    )

    payload = {
        "status": "failed" if issues else "ok",
        "checked_at": date.today().isoformat(),
        "network_checked": not options.no_network,
        "required_files": required_files,
        "source_ids": source_ids,
        "summary": {
            "sources_total": len(sources),
            "official_sources": official_count,
            "provider_official_sources": provider_count,
            "local_content_sources": local_count,
            "r2_provider_sources_total": len(r2_providers),
            "r2_provider_sources_confirmed": r2_confirmed,
            "r2_provider_sources_pending": r2_pending,
        },
        "issues": issues,
        "warnings": warnings,
        "reachability": reachability,
    }
    return payload


def render_check_markdown(payload: dict[str, Any]) -> str:
    lines = ["# 官方来源同步 Check", "", f"- status: `{payload['status']}`", f"- checked_at: `{payload['checked_at']}`", f"- network_checked: `{str(payload['network_checked']).lower()}`", ""]
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
    lines.append("## Warnings")
    if payload["warnings"]:
        lines.extend(f"- {warning}" for warning in payload["warnings"])
    else:
        lines.append("- none")
    lines.append("")
    return "\n".join(lines)


def render_digest(options: CheckOptions) -> str:
    registry = load_registry(options.registry)
    payload = validate(options)
    sources = source_list(registry)
    provider_block = registry.get("provider_sources_to_fill_in_r2", {})
    providers = provider_block.get("providers", []) if isinstance(provider_block, dict) else []

    lines = [
        "# 官方来源同步 Digest",
        "",
        f"生成日期：{date.today().isoformat()}",
        "",
        "## R1 当前状态",
        "",
        f"- check_status: `{payload['status']}`",
        f"- registered_sources: {payload['summary']['sources_total']}",
        f"- official_sources: {payload['summary']['official_sources']}",
        f"- local_content_sources: {payload['summary']['local_content_sources']}",
        "- side_effect: `none`",
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
    lines.extend(["", "## R2 官方来源确认状态", ""])
    if providers:
        lines.extend(["| ID | Area | Status | Source URLs |", "|---|---|---|---|"])
        for provider in providers:
            source_count = len(provider.get("source_urls") or [])
            lines.append(
                f"| `{provider.get('id', '')}` | {provider.get('area', '')} | `{provider.get('status', '')}` | {source_count} |"
            )
    else:
        lines.append("- none")
    lines.extend([
        "",
        "## 维护者下一步",
        "",
        "1. R1 已完成 registry / policy / 脚本基座。",
        "2. R2 已把国内模型 / 部署页面的厂商官方来源写回 registry 与页面同步记录。",
        "3. 后续如发现本仓内容与官方来源冲突，先开 review issue，再改正文。",
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
        # Keep digest clean from internal execution logs. Credential prohibition phrases are allowed as policy text.
        digest = digest.replace(term, "[internal-term-redacted]")
    return digest


def render_issue_body(options: CheckOptions) -> str:
    digest = render_digest(options)
    return "\n".join([
        "## 背景",
        "R1 已建立官方来源 registry / policy；R2 已确认国内模型与部署页面的厂商官方来源，并把来源写回 registry 与页面同步记录。",
        "",
        "## R2 digest",
        "",
        digest,
        "",
        "## 建议处理",
        "",
        "- [ ] 后续修改国内模型页面前，先复查 registry 中对应 source_urls。",
        "- [ ] 后续修改国内部署页面前，先复查 registry 中对应 source_urls。",
        "- [ ] 对任何影响用户操作的正文改动记录 source / checked_at / affected_docs。",
        "",
        "## Dry-run 声明",
        "本输出仅用于本地 dry-run；未调用 GitHub API，未创建远端 issue。",
    ])


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
    parser.add_argument("--policy", type=Path, default=DEFAULT_POLICY)
    parser.add_argument("--human-registry", type=Path, default=DEFAULT_HUMAN_REGISTRY)
    parser.add_argument("--no-network", action="store_true", help="Skip reachability checks")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Official-source sync helper")
    add_common_options(parser)
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="Validate registry and policy")
    add_common_options(check)
    check.add_argument("--format", choices=("markdown", "json"), default="markdown")
    check.add_argument("--output")

    digest = sub.add_parser("digest", help="Render Markdown digest")
    add_common_options(digest)
    digest.add_argument("--output")

    issue = sub.add_parser("issue", help="Render issue body; only dry-run is supported")
    add_common_options(issue)
    issue.add_argument("--dry-run", action="store_true", help="Required; never creates a remote issue")
    issue.add_argument("--format", choices=("markdown", "json"), default="markdown")
    issue.add_argument("--output")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    options = CheckOptions(args.registry, args.policy, args.human_registry, args.no_network)

    if args.command == "check":
        payload = validate(options)
        text = json.dumps(payload, ensure_ascii=False, indent=2) if args.format == "json" else render_check_markdown(payload)
        write_or_print(text, args.output)
        return 0 if payload["status"] == "ok" else 1

    if args.command == "digest":
        write_or_print(render_digest(options), args.output)
        return 0

    if args.command == "issue":
        if not args.dry_run:
            print("Refusing to create remote issue. Re-run with --dry-run.", file=sys.stderr)
            return 2
        body = render_issue_body(options)
        if args.format == "json":
            text = json.dumps(
                {
                    "dry_run": True,
                    "side_effect": "none",
                    "title": "R1 官方来源同步：R2 官方来源确认待办",
                    "body": body,
                },
                ensure_ascii=False,
                indent=2,
            )
        else:
            text = "\n".join([
                "# R1 官方来源同步：R2 官方来源确认待办",
                "",
                "dry_run: true",
                "side_effect: none",
                "",
                body,
            ])
        write_or_print(text, args.output)
        return 0

    parser.error("unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
