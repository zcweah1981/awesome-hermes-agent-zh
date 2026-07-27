#!/usr/bin/env python3
"""Ratchet existing content-quality debt without inventing source evidence."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
ROUTE_MAP = REPO_ROOT / "governance" / "site-route-map.yaml"
BASELINE = REPO_ROOT / "governance" / "content-quality-baseline.yaml"
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".avif", ".webp"}


def route_entries() -> list[dict]:
    data = yaml.safe_load(ROUTE_MAP.read_text(encoding="utf-8")) or {}
    return data.get("routes", [])


def has_numbered_emoji_h1(markdown: str) -> bool:
    first_h1 = next((line.strip() for line in markdown.splitlines() if line.startswith("# ")), "")
    if not first_h1:
        return False
    title = first_h1[2:].strip()
    parts = title.split(maxsplit=1)
    return len(parts) == 2 and len(parts[0]) <= 4 and parts[1][:2].isdigit() and parts[1][2:3] in {"-", "—"}


def has_navigation_footer(markdown: str) -> bool:
    tail = markdown[-1600:]
    return "## ➡️ 下一步" in tail and any(
        marker in tail for marker in ("上一步", "上一阶段", "上一篇", "回到", "返回")
    )


def unused_webp_paths() -> list[str]:
    text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for pattern in ("*.md", "*.yaml", "*.yml")
        for path in REPO_ROOT.rglob(pattern)
        if ".git" not in path.parts and path != BASELINE
    )
    webp_files = [
        path
        for root in (REPO_ROOT / "docs", REPO_ROOT / "assets")
        for path in root.rglob("*.webp")
    ]
    return sorted(
        path.relative_to(REPO_ROOT).as_posix()
        for path in webp_files
        if path.name not in text and path.relative_to(REPO_ROOT).as_posix() not in text
    )


def collect_issues() -> dict[str, list[str]]:
    routes = route_entries()
    issues: dict[str, list[str]] = {
        "h1_exceptions": [],
        "navigation_exceptions": [],
        "source_refs_exceptions": [],
        "source_review_exceptions": [],
        "unused_webp_exceptions": unused_webp_paths(),
    }

    for route in routes:
        source = route["source"]
        markdown = (REPO_ROOT / source).read_text(encoding="utf-8")
        if not has_numbered_emoji_h1(markdown):
            issues["h1_exceptions"].append(source)
        if not has_navigation_footer(markdown):
            issues["navigation_exceptions"].append(source)
        if not route.get("source_refs"):
            issues["source_refs_exceptions"].append(source)
        if not route.get("source_review"):
            issues["source_review_exceptions"].append(source)

    return {key: sorted(value) for key, value in issues.items()}


def validate_image_formats() -> None:
    invalid = sorted(
        path.relative_to(REPO_ROOT).as_posix()
        for root in (REPO_ROOT / "docs", REPO_ROOT / "assets")
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES - {".webp"}
    )
    if invalid:
        raise SystemExit("non-WebP public images:\n" + "\n".join(invalid))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-baseline", action="store_true")
    args = parser.parse_args()
    validate_image_formats()
    issues = collect_issues()

    if args.write_baseline:
        payload = {"schema_version": 1, **issues}
        BASELINE.write_text(
            yaml.safe_dump(payload, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
            newline="\n",
        )
        print(f"wrote content quality baseline to {BASELINE.relative_to(REPO_ROOT).as_posix()}")
        return 0

    baseline = yaml.safe_load(BASELINE.read_text(encoding="utf-8")) or {}
    expected = {key: set(baseline.get(key, [])) for key in issues}
    regressions = {
        key: sorted(set(values) - expected[key])
        for key, values in issues.items()
        if set(values) - expected[key]
    }
    if regressions:
        for key, values in regressions.items():
            print(f"{key}: {len(values)} new exception(s)")
            for value in values:
                print(f"  - {value}")
        print("content quality debt increased; fix the regression or update the reviewed baseline")
        return 1

    print(
        "content quality baseline verified "
        + " ".join(f"{key}={len(value)}" for key, value in issues.items())
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
