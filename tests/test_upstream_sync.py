import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "upstream_sync.py"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def test_check_validates_registry_policy_and_outputs_json():
    result = run_cli("check", "--no-network", "--format", "json")

    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["status"] == "ok"
    assert payload["network_checked"] is False
    assert payload["required_files"]["governance/upstream-source-registry.yaml"] == "ok"
    assert payload["required_files"]["governance/upstream-sync-policy.md"] == "ok"
    assert payload["summary"]["official_sources"] >= 2
    assert "hermes-official-docs" in payload["source_ids"]


def test_digest_renders_human_markdown_without_internal_logs():
    result = run_cli("digest", "--no-network")

    assert result.returncode == 0, result.stderr
    body = result.stdout
    assert "# 官方来源同步 Digest" in body
    assert "hermes-official-docs" in body
    assert "R2 待补官方来源" in body
    assert "dispatch" not in body.lower()
    assert "worker_run" not in body.lower()


def test_issue_dry_run_never_calls_github_and_marks_no_side_effect():
    result = run_cli("issue", "--dry-run", "--format", "json", "--no-network")

    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["dry_run"] is True
    assert payload["side_effect"] == "none"
    assert payload["title"].startswith("R1 官方来源同步")
    assert "gh issue create" not in payload["body"]
    assert "R2 待补官方来源" in payload["body"]


def test_check_fails_when_registry_missing_required_official_source(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    registry.write_text(
        "updated: '2026-05-02'\n"
        "source_tiers:\n"
        "  official:\n"
        "    required_before_public_claim: true\n"
        "sources:\n"
        "  - id: content-repo\n"
        "    tier: local_content\n"
        "    name: local\n"
        "    url: https://example.com\n",
        encoding="utf-8",
    )
    result = run_cli("check", "--registry", str(registry), "--no-network", "--format", "json")

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["status"] == "failed"
    assert any("official source" in issue for issue in payload["issues"])


def test_upstream_sync_workflow_runs_weekly_manually_and_creates_issue():
    workflow = REPO / ".github" / "workflows" / "upstream-sync-check.yml"
    assert workflow.exists()

    body = workflow.read_text(encoding="utf-8")
    assert "name: upstream-sync-check" in body
    assert "workflow_dispatch:" in body
    assert "schedule:" in body
    assert "issues: write" in body
    assert "python3 scripts/upstream_sync.py check" in body
    assert "python3 scripts/upstream_sync.py issue --dry-run --format json" in body
    assert "gh issue create" in body
    assert "upstream-sync" in body
    assert "GITHUB_TOKEN" in body
