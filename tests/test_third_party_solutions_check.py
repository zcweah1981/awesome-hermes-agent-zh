import json
import subprocess
import sys
from pathlib import Path

import yaml


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "third_party_solutions_check.py"
REGISTRY = REPO / "governance" / "third-party-solutions-registry.yaml"
WORKFLOW = REPO / ".github" / "workflows" / "third-party-solutions-weekly-check.yml"
LOCAL_DOC = REPO / "docs/02-现成方案/01-内容创作与发布/05-X-Twitter 内容与互动助手.md"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def test_third_party_registry_schema_includes_hermes_tweet_contract():
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))

    assert registry["schema_version"] == 1
    solutions = registry["solutions"]
    hermes_tweet = next(item for item in solutions if item["id"] == "hermes-tweet")

    for field in ("local_doc", "source", "version", "last_checked_at"):
        assert hermes_tweet[field]
    assert hermes_tweet["local_doc"] == LOCAL_DOC.relative_to(REPO).as_posix()
    assert hermes_tweet["source"]["github_repo"] == "Xquik-dev/hermes-tweet"
    assert hermes_tweet["source"]["pypi_package"] == "hermes-tweet"
    assert hermes_tweet["source"]["docs_url"] == "https://docs.xquik.com/guides/hermes-tweet"
    assert hermes_tweet["source"]["agent_skill_url"] == "https://agentskill.sh/@xquik-dev/hermes-tweet"
    assert hermes_tweet["version"]["recorded_pypi"] == "0.1.6"
    assert hermes_tweet["review_policy"]["auto_update_docs"] is False


def test_checker_outputs_markdown_report_and_issue_payload_without_auto_doc_changes(tmp_path: Path):
    before = LOCAL_DOC.read_text(encoding="utf-8")
    report = tmp_path / "third-party-report.md"
    payload = tmp_path / "issue-payload.json"

    check_result = run_cli("check", "--no-network", "--output", str(report))
    issue_result = run_cli("issue", "--no-network", "--format", "json", "--output", str(payload))

    assert check_result.returncode == 0, check_result.stderr
    assert issue_result.returncode == 0, issue_result.stderr
    assert LOCAL_DOC.read_text(encoding="utf-8") == before
    report_body = report.read_text(encoding="utf-8")
    assert "# Third-party Solutions Weekly Check" in report_body
    assert "hermes-tweet" in report_body
    issue_payload = json.loads(payload.read_text(encoding="utf-8"))
    assert issue_payload["side_effect"] == "none"
    assert issue_payload["would_create_issue"] is False
    assert issue_payload["document_update"] == "forbidden"
    assert "gh issue create" not in issue_payload["body"]


def test_issue_payload_is_review_only_when_versions_change(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    registry.write_text(
        "schema_version: 1\n"
        "solutions:\n"
        "  - id: hermes-tweet\n"
        "    name: Hermes Tweet\n"
        "    local_doc: docs/02-现成方案/01-内容创作与发布/05-X-Twitter 内容与互动助手.md\n"
        "    source:\n"
        "      github_repo: Xquik-dev/hermes-tweet\n"
        "      github_url: https://github.com/Xquik-dev/hermes-tweet\n"
        "      pypi_package: hermes-tweet\n"
        "      pypi_url: https://pypi.org/project/hermes-tweet/\n"
        "      docs_url: https://docs.xquik.com/guides/hermes-tweet\n"
        "      agent_skill_url: https://agentskill.sh/@xquik-dev/hermes-tweet\n"
        "    version:\n"
        "      recorded_pypi: 0.1.6\n"
        "      recorded_github_tag: v0.1.6\n"
        "      latest_pypi: 0.2.0\n"
        "      latest_github_tag: v0.2.0\n"
        "    last_checked_at: '2026-05-16'\n"
        "    review_policy:\n"
        "      auto_update_docs: false\n",
        encoding="utf-8",
    )

    result = run_cli("issue", "--registry", str(registry), "--no-network", "--format", "json")

    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert payload["would_create_issue"] is True
    assert payload["side_effect"] == "none"
    assert payload["document_update"] == "forbidden"
    assert "hermes-tweet" in payload["title"]
    assert "0.2.0" in payload["body"]
    assert "只创建 review issue" in payload["body"]


def test_weekly_workflow_supports_manual_schedule_token_safe_dry_run():
    body = WORKFLOW.read_text(encoding="utf-8")

    assert "name: third-party-solutions-weekly-check" in body
    assert "workflow_dispatch:" in body
    assert "schedule:" in body
    assert "cron:" in body
    assert "issues: write" in body
    assert "python3 scripts/third_party_solutions_check.py check" in body
    assert "python3 scripts/third_party_solutions_check.py issue --format json" in body
    assert "GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}" in body
    assert "if [ -z \"${GH_TOKEN:-}\" ]" in body
    assert "gh issue create" in body
    assert "--body-file third-party-issue.md" in body
