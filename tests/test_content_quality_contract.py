from scripts.content_quality_check import (
    BASELINE,
    collect_issues,
    route_entries,
    validate_image_formats,
)

import yaml


def test_content_quality_debt_does_not_exceed_reviewed_baseline():
    validate_image_formats()
    baseline = yaml.safe_load(BASELINE.read_text(encoding="utf-8"))
    issues = collect_issues()

    for key, values in issues.items():
        assert set(values) <= set(baseline.get(key, []))


def test_issue_routes_keep_official_source_mapping_and_review_state():
    expected_sources = {
        "docs/05-遇到问题/01-总览.md",
        "docs/05-遇到问题/02-安装更新与环境问题.md",
        "docs/05-遇到问题/03-模型 Provider 与自定义 endpoint 问题.md",
        "docs/05-遇到问题/04-CLI TUI 与会话问题.md",
        "docs/05-遇到问题/05-Gateway Messaging 与推送问题.md",
        "docs/05-遇到问题/06-Tools Skills MCP 问题.md",
        "docs/05-遇到问题/07-配置 Profiles 与环境隔离问题.md",
        "docs/05-遇到问题/08-Docker Nix SSH 与远程后端问题.md",
    }
    issue_routes = {
        route["source"]: route
        for route in route_entries()
        if route["source"] in expected_sources
    }

    assert set(issue_routes) == expected_sources
    for source, route in issue_routes.items():
        assert route["source_refs"]["local"] == ["content-repo"], source
        assert "hermes-official-docs" in route["source_refs"]["official"], source
        assert route["source_review"]["state"] in {
            "needs-official-check",
            "official-source-confirmed",
        }, source
        assert route["source_review"]["checked_at"] == "2026-07-27", source


def test_first_seo_provider_routes_keep_confirmed_official_source_mapping():
    expected = {
        "docs/03-国内落地/02-国内模型/02-阿里云百炼Token plan.md": "aliyun-bailian",
        "docs/03-国内落地/02-国内模型/03-腾讯云Token Plan.md": "tencent-cloud-models",
    }
    provider_routes = {
        route["source"]: route
        for route in route_entries()
        if route["source"] in expected
    }

    assert set(provider_routes) == set(expected)
    for source, provider_id in expected.items():
        route = provider_routes[source]
        assert route["source_refs"]["local"] == ["content-repo"], source
        assert "hermes-official-docs" in route["source_refs"]["official"], source
        assert route["source_refs"]["provider_pending"] == [provider_id], source
        assert (
            route["source_review"]["state"]
            == "provider-official-source-confirmed"
        ), source
        assert route["source_review"]["checked_at"] == "2026-07-28", source
