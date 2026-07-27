import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"


def read(name: str) -> str:
    return (WORKFLOWS / name).read_text(encoding="utf-8").replace("\r\n", "\n")


def test_only_pull_request_ci_gate_runs_automatically():
    content_check = read("content-check.yml")
    assert "\n  pull_request:\n" in content_check
    assert "\n  push:" not in content_check
    assert "\n  schedule:" not in content_check

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


def test_manual_site_dispatch_does_not_repeat_content_validation():
    workflow = read("trigger-hermes-zh-content-sync.yml")
    assert "actions/checkout@" not in workflow
    assert "pip install" not in workflow
    assert "normalize_route_order.py" not in workflow
    assert "content_quality_check.py" not in workflow
    assert "Dispatch hermes-zh site content sync" in workflow


def test_ci_documentation_defines_zero_scheduled_runs():
    docs = (ROOT / "docs" / "ci.md").read_text(encoding="utf-8")
    assert "Actions 月度预算" in docs
    assert "仅 `CI Gate` 自动运行" in docs
    assert "零 schedule" in docs


def test_all_third_party_actions_are_pinned_to_immutable_shas():
    for workflow in (ROOT / ".github" / "workflows").glob("*.yml"):
        body = workflow.read_text(encoding="utf-8")
        for action in re.findall(r"uses:\s*([^\s]+)", body):
            if action.startswith("./"):
                continue
            assert re.search(r"@[0-9a-f]{40}$", action), f"{workflow.name}: {action}"
