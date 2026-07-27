#!/usr/bin/env python3
"""Keep route-map order aligned with its reviewed physical sequence."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ROUTE_MAP = REPO_ROOT / "governance" / "site-route-map.yaml"
ROUTE_START = re.compile(r"^- source:\s*(.+?)\s*$")
ORDER_LINE = re.compile(r"^  order:\s*.+$")
GOVERNANCE_ONLY_SOURCE = "packs/README.md"


def normalized_route_map(raw: str) -> tuple[str, int]:
    lines = raw.splitlines()
    contract_index = next(
        (index for index, line in enumerate(lines) if line.startswith("source_mapping_contract:")),
        len(lines),
    )
    prefix = lines[:contract_index]
    suffix = lines[contract_index:]
    route_indexes = [index for index, line in enumerate(prefix) if ROUTE_START.match(line)]

    if not route_indexes:
        raise ValueError("site-route-map.yaml contains no route entries")

    output = prefix[: route_indexes[0]]
    kept = 0

    for position, start in enumerate(route_indexes):
        end = route_indexes[position + 1] if position + 1 < len(route_indexes) else len(prefix)
        block = prefix[start:end]
        source_match = ROUTE_START.match(block[0])
        source = source_match.group(1) if source_match else ""

        if source == GOVERNANCE_ONLY_SOURCE:
            continue
        if not source.startswith("docs/") or not source.endswith(".md"):
            raise ValueError(f"published route source must be docs/**/*.md: {source}")

        kept += 1
        order_indexes = [index for index, line in enumerate(block) if ORDER_LINE.match(line)]
        if len(order_indexes) != 1:
            raise ValueError(f"route {source} must contain exactly one order field")
        block[order_indexes[0]] = f"  order: {kept}"
        output.extend(block)

    output.extend(suffix)
    return "\n".join(output) + "\n", kept


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="rewrite route map in place")
    args = parser.parse_args()

    raw = ROUTE_MAP.read_text(encoding="utf-8")
    normalized, count = normalized_route_map(raw)

    if args.write:
        ROUTE_MAP.write_text(normalized, encoding="utf-8", newline="\n")
        print(f"normalized {count} published doc routes")
        return 0

    if raw.replace("\r\n", "\n") != normalized:
        print("route map order is not normalized; run scripts/normalize_route_order.py --write")
        return 1

    print(f"verified {count} published doc routes with unique global order")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
