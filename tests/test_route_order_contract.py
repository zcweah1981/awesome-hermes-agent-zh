from pathlib import Path

import yaml

from scripts.normalize_route_order import normalized_route_map


REPO = Path(__file__).resolve().parents[1]
ROUTE_MAP = REPO / "governance" / "site-route-map.yaml"


def test_route_map_is_normalized_and_contains_only_published_docs():
    raw = ROUTE_MAP.read_text(encoding="utf-8")
    normalized, count = normalized_route_map(raw)
    data = yaml.safe_load(raw)
    routes = data["routes"]

    assert raw.replace("\r\n", "\n") == normalized
    assert count == len(routes)
    assert [route["order"] for route in routes] == list(range(1, count + 1))
    assert all(route["source"].startswith("docs/") and route["source"].endswith(".md") for route in routes)
    assert all(route["source"] != "packs/README.md" for route in routes)
    assert all(route["slug"] != "/packs" for route in routes)
