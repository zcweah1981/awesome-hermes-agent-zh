#!/usr/bin/env python3
"""Third-party solution weekly checker for awesome-hermes-agent-zh.

Side-effect contract:
- `check` validates registry schema and renders a Markdown/JSON report.
- `issue` renders a review issue payload only.
- This script never edits local docs and never calls GitHub issue APIs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = REPO_ROOT / "governance" / "third-party-solutions-registry.yaml"
REQUIRED_SOLUTION_FIELDS = ("id", "name", "local_doc", "source", "version", "last_checked_at")
REQUIRED_SOURCE_FIELDS = ("github_repo", "github_url", "pypi_package", "pypi_url", "docs_url")
REQUIRED_VERSION_FIELDS = ("recorded_pypi",)
USER_AGENT = "awesome-hermes-agent-zh-third-party-check/1.0"


@dataclass(frozen=True)
class Options:
    registry: Path
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
        raise RuntimeError("PyYAML is required to parse third-party-solutions-registry.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("registry YAML root must be a mapping")
    return data


def solution_list(registry: dict[str, Any]) -> list[dict[str, Any]]:
    values = registry.get("solutions")
    if not isinstance(values, list):
        return []
    return [item for item in values if isinstance(item, dict)]


def http_json(url: str, timeout: float = 8.0) -> dict[str, Any] | None:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(req, timeout=timeout) as res:  # nosec: registry-controlled public URLs.
        return json.loads(res.read().decode("utf-8"))


def head_url(url: str, timeout: float = 8.0) -> dict[str, Any]:
    req = Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=timeout) as res:  # nosec: registry-controlled public URLs.
            return {"status": "ok", "code": res.status}
    except HTTPError as exc:
        if exc.code in {403, 405}:
            return {"status": "warning", "code": exc.code, "message": "HEAD blocked"}
        return {"status": "failed", "code": exc.code, "message": str(exc)}
    except URLError as exc:
        return {"status": "failed", "message": str(exc.reason)}
    except Exception as exc:  # pragma: no cover
        return {"status": "failed", "message": str(exc)}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fetch_github_state(repo: str) -> dict[str, Any]:
    state: dict[str, Any] = {}
    repo_meta = http_json(f"https://api.github.com/repos/{repo}") or {}
    state["pushed_at"] = repo_meta.get("pushed_at")
    state["default_branch"] = repo_meta.get("default_branch")
    try:
        release = http_json(f"https://api.github.com/repos/{repo}/releases/latest") or {}
        state["latest_release"] = release.get("tag_name")
    except Exception:
        state["latest_release"] = None
    try:
        tags = http_json(f"https://api.github.com/repos/{repo}/tags") or []
        if isinstance(tags, list) and tags:
            state["latest_tag"] = tags[0].get("name")
    except Exception:
        state["latest_tag"] = None
    try:
        readme_req = Request(
            f"https://raw.githubusercontent.com/{repo}/{state.get('default_branch') or 'main'}/README.md",
            headers={"User-Agent": USER_AGENT},
        )
        with urlopen(readme_req, timeout=8) as res:  # nosec: public GitHub URL from registry.
            state["readme_fingerprint"] = sha256_text(res.read().decode("utf-8", errors="replace"))
    except Exception:
        state["readme_fingerprint"] = None
    return state


def fetch_pypi_state(package: str) -> dict[str, Any]:
    data = http_json(f"https://pypi.org/pypi/{package}/json") or {}
    info = data.get("info", {}) if isinstance(data, dict) else {}
    metadata = {
        "name": info.get("name"),
        "version": info.get("version"),
        "summary": info.get("summary"),
        "requires_python": info.get("requires_python"),
        "project_urls": info.get("project_urls"),
    }
    return {
        "version": info.get("version"),
        "package_metadata_fingerprint": sha256_text(json.dumps(metadata, sort_keys=True, ensure_ascii=False)),
    }


def collect_solution_state(solution: dict[str, Any], no_network: bool) -> dict[str, Any]:
    source = solution.get("source", {}) if isinstance(solution.get("source"), dict) else {}
    version = solution.get("version", {}) if isinstance(solution.get("version"), dict) else {}
    latest: dict[str, Any] = {
        "github_latest_release": version.get("latest_github_release") or version.get("latest_github_tag"),
        "github_latest_tag": version.get("latest_github_tag"),
        "github_pushed_at": version.get("github_pushed_at"),
        "pypi_version": version.get("latest_pypi") or version.get("recorded_pypi"),
        "docs_reachable": "not_checked",
        "readme_fingerprint": version.get("readme_fingerprint"),
        "package_metadata_fingerprint": version.get("package_metadata_fingerprint"),
    }
    warnings: list[str] = []
    if no_network:
        return {"latest": latest, "warnings": warnings}
    try:
        gh_state = fetch_github_state(str(source.get("github_repo")))
        latest.update(
            {
                "github_latest_release": gh_state.get("latest_release") or latest["github_latest_release"],
                "github_latest_tag": gh_state.get("latest_tag") or latest["github_latest_tag"],
                "github_pushed_at": gh_state.get("pushed_at"),
                "readme_fingerprint": gh_state.get("readme_fingerprint"),
            }
        )
    except Exception as exc:
        warnings.append(f"{solution.get('id')}: GitHub check failed: {exc}")
    try:
        pypi_state = fetch_pypi_state(str(source.get("pypi_package")))
        latest.update(
            {
                "pypi_version": pypi_state.get("version") or latest["pypi_version"],
                "package_metadata_fingerprint": pypi_state.get("package_metadata_fingerprint"),
            }
        )
    except Exception as exc:
        warnings.append(f"{solution.get('id')}: PyPI check failed: {exc}")
    docs_url = source.get("docs_url")
    if isinstance(docs_url, str) and docs_url.startswith("http"):
        latest["docs_reachable"] = head_url(docs_url)
    return {"latest": latest, "warnings": warnings}


def compare_solution(solution: dict[str, Any], latest: dict[str, Any]) -> list[str]:
    version = solution.get("version", {}) if isinstance(solution.get("version"), dict) else {}
    changes: list[str] = []
    pairs = (
        ("PyPI version", version.get("recorded_pypi"), latest.get("pypi_version")),
        ("GitHub latest tag", version.get("recorded_github_tag"), latest.get("github_latest_tag")),
        ("GitHub pushed_at", version.get("github_pushed_at"), latest.get("github_pushed_at")),
        ("README fingerprint", version.get("readme_fingerprint"), latest.get("readme_fingerprint")),
        ("package metadata fingerprint", version.get("package_metadata_fingerprint"), latest.get("package_metadata_fingerprint")),
    )
    for label, recorded, current in pairs:
        if recorded not in (None, "") and current not in (None, "") and str(recorded) != str(current):
            changes.append(f"{label}: recorded `{recorded}` -> current `{current}`")
    docs_status = latest.get("docs_reachable")
    if isinstance(docs_status, dict) and docs_status.get("status") == "failed":
        changes.append(f"Docs reachability failed: {docs_status.get('message', docs_status)}")
    return changes


def validate(options: Options) -> dict[str, Any]:
    issues: list[str] = []
    warnings: list[str] = []
    registry: dict[str, Any] = {}
    solutions: list[dict[str, Any]] = []
    try:
        registry = load_registry(options.registry)
        solutions = solution_list(registry)
    except Exception as exc:
        issues.append(f"registry parse failed: {exc}")

    if registry and registry.get("schema_version") != 1:
        issues.append("registry schema_version must be 1")
    if not solutions:
        issues.append("registry must contain a solutions list")

    seen: set[str] = set()
    source_ids: list[str] = []
    checks: list[dict[str, Any]] = []
    for solution in solutions:
        sid = str(solution.get("id", ""))
        source_ids.append(sid)
        if sid in seen:
            issues.append(f"duplicate solution id: {sid}")
        seen.add(sid)
        missing = [field for field in REQUIRED_SOLUTION_FIELDS if not solution.get(field)]
        if missing:
            issues.append(f"solution {sid or '<missing-id>'} missing fields: {', '.join(missing)}")
        source = solution.get("source", {}) if isinstance(solution.get("source"), dict) else {}
        version = solution.get("version", {}) if isinstance(solution.get("version"), dict) else {}
        for field in REQUIRED_SOURCE_FIELDS:
            if not source.get(field):
                issues.append(f"solution {sid} source missing field: {field}")
        for field in REQUIRED_VERSION_FIELDS:
            if not version.get(field):
                issues.append(f"solution {sid} version missing field: {field}")
        local_doc = REPO_ROOT / str(solution.get("local_doc", ""))
        if solution.get("local_doc") and not local_doc.exists():
            issues.append(f"solution {sid} local_doc not found: {solution.get('local_doc')}")
        if solution.get("review_policy", {}).get("auto_update_docs") is not False:
            issues.append(f"solution {sid} review_policy.auto_update_docs must be false")
        state = collect_solution_state(solution, options.no_network)
        warnings.extend(state["warnings"])
        changes = compare_solution(solution, state["latest"])
        checks.append({"id": sid, "local_doc": solution.get("local_doc"), "latest": state["latest"], "changes": changes})

    if "hermes-tweet" not in source_ids:
        issues.append("registry missing required third-party source: hermes-tweet")

    change_count = sum(len(item["changes"]) for item in checks)
    return {
        "status": "failed" if issues else "ok",
        "checked_at": date.today().isoformat(),
        "network_checked": not options.no_network,
        "registry": repo_relative(options.registry),
        "source_ids": source_ids,
        "summary": {"solutions_total": len(solutions), "changes_detected": change_count, "document_updates": 0},
        "checks": checks,
        "issues": issues,
        "warnings": warnings,
        "side_effect": "none",
        "document_update": "forbidden",
    }


def render_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Third-party Solutions Weekly Check",
        "",
        f"- status: `{payload['status']}`",
        f"- checked_at: `{payload['checked_at']}`",
        f"- network_checked: `{str(payload['network_checked']).lower()}`",
        "- side_effect: `none`",
        "- document_update: `forbidden`",
        "",
        "## Summary",
    ]
    for key, value in payload["summary"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Solutions", "", "| ID | Local doc | Changes |", "|---|---|---|"])
    for item in payload["checks"]:
        change_text = "<br>".join(item["changes"]) if item["changes"] else "none"
        lines.append(f"| `{item['id']}` | `{item['local_doc']}` | {change_text} |")
    lines.extend(["", "## Issues"])
    lines.extend(f"- {issue}" for issue in payload["issues"]) if payload["issues"] else lines.append("- none")
    lines.extend(["", "## Warnings"])
    lines.extend(f"- {warning}" for warning in payload["warnings"]) if payload["warnings"] else lines.append("- none")
    lines.extend(["", "## Governance", "", "检测到版本、README/package metadata 或 Docs 可访问性变化时，只创建 review issue / 输出 issue payload；不得自动改正文。"])
    return "\n".join(lines) + "\n"


def render_issue_payload(payload: dict[str, Any]) -> dict[str, Any]:
    changed = [item for item in payload["checks"] if item["changes"]]
    if changed:
        first = changed[0]["id"]
        title = f"[third-party-review] {first} source update review required"
    else:
        title = "[third-party-review] weekly source check report"
    lines = [
        "## 背景",
        "第三方方案 source registry weekly check 已完成。检测到版本/元数据/可访问性变化时，本 payload 只创建 review issue / 输出 issue payload，不自动改正文。",
        "",
        "## 变更检测",
    ]
    if changed:
        for item in changed:
            lines.append(f"### {item['id']}")
            lines.extend(f"- {change}" for change in item["changes"])
    else:
        lines.append("- 本次未发现需要 review 的版本或元数据变化。")
    lines.extend([
        "",
        "## 维护动作",
        "- [ ] 人工复查 GitHub latest release/tag/pushed_at。",
        "- [ ] 人工复查 PyPI version 与 package metadata。",
        "- [ ] 人工打开 Docs URL 确认可访问性。",
        "- [ ] 如确认正文需要更新，再单独提交内容 PR。",
        "",
        "## 安全声明",
        "- side_effect: none（脚本不调用 GitHub API）",
        "- document_update: forbidden（脚本不自动改正文）",
        "- GitHub Actions 中 issue 创建必须从 secrets.GITHUB_TOKEN 读取 token；无 token 时 dry-run/report。",
    ])
    return {
        "dry_run": True,
        "side_effect": "none",
        "document_update": "forbidden",
        "would_create_issue": bool(changed),
        "title": title,
        "body": "\n".join(lines),
        "changes_detected": payload["summary"]["changes_detected"],
    }


def write_or_print(text: str, output: str | None) -> None:
    if output:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path}")
    else:
        print(text, end="" if text.endswith("\n") else "\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Third-party solution registry checker")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--no-network", action="store_true")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("check", "issue"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
        cmd.add_argument("--no-network", action="store_true")
        cmd.add_argument("--format", choices=("markdown", "json"), default="markdown")
        cmd.add_argument("--output")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    options = Options(args.registry, args.no_network)
    payload = validate(options)
    if args.command == "check":
        text = json.dumps(payload, ensure_ascii=False, indent=2) if args.format == "json" else render_report(payload)
        write_or_print(text, args.output)
        return 0 if payload["status"] == "ok" else 1
    if args.command == "issue":
        issue_payload = render_issue_payload(payload)
        text = json.dumps(issue_payload, ensure_ascii=False, indent=2) if args.format == "json" else f"# {issue_payload['title']}\n\n{issue_payload['body']}\n"
        write_or_print(text, args.output)
        return 0 if payload["status"] == "ok" else 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
