import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"


def read(name: str) -> str:
    return (WORKFLOWS / name).read_text(encoding="utf-8").replace("\r\n", "\n")


def test_no_ci_workflow_and_all_maintenance_tools_are_manual_only():
    assert not (WORKFLOWS / "content-check.yml").exists()
    for name in [
        "link-check.yml",
        "third-party-solutions-weekly-check.yml",
        "trigger-hermes-zh-content-sync.yml",
        "upstream-sync-check.yml",
    ]:
        workflow = read(name)
        assert "\n  workflow_dispatch:" in workflow
        assert "\n  push:" not in workflow
        assert "\n  pull_request:" not in workflow
        assert "\n  schedule:" not in workflow
        assert "\n  repository_dispatch:" not in workflow


def test_manual_site_dispatch_does_not_repeat_content_validation():
    workflow = read("trigger-hermes-zh-content-sync.yml")
    assert "actions/checkout@" not in workflow
    assert "pip install" not in workflow
    assert "normalize_route_order.py" not in workflow
    assert "content_quality_check.py" not in workflow
    assert "Dispatch hermes-zh site content sync" in workflow
    assert "/actions/workflows/${TARGET_WORKFLOW}/dispatches" in workflow
    assert "TARGET_WORKFLOW: content-auto-sync.yml" in workflow
    assert "'ref': 'main'" in workflow
    for input_name in ["content_repo", "content_ref", "content_sha", "source_actor"]:
        assert f"'{input_name}':" in workflow
    assert "repository_dispatch" not in workflow


def test_direct_delivery_documentation_has_no_pr_or_ci_gate():
    docs = (ROOT / "docs" / "ci.md").read_text(encoding="utf-8")
    assert "Direct Delivery v3.1" in docs
    assert "不保留 Pull Request 门禁" in docs
    assert "GitHub Actions CI" in docs
    assert "不作为 commit、push、内容同步或生产部署的前置条件" in docs


def test_all_third_party_actions_are_pinned_to_immutable_shas():
    for workflow in (ROOT / ".github" / "workflows").glob("*.yml"):
        body = workflow.read_text(encoding="utf-8")
        for action in re.findall(r"uses:\s*([^\s]+)", body):
            if action.startswith("./"):
                continue
            assert re.search(r"@[0-9a-f]{40}$", action), f"{workflow.name}: {action}"
