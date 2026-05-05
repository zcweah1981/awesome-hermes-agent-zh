import re
from pathlib import Path

import yaml


REPO = Path(__file__).resolve().parents[1]
WORKFLOW = REPO / ".github" / "workflows" / "trigger-hermes-zh-content-sync.yml"


def workflow_text() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_trigger_workflow_is_valid_yaml_and_dispatches_expected_repo_event():
    body = workflow_text()
    parsed = yaml.safe_load(body)

    assert parsed["name"] == "trigger-hermes-zh-content-sync"
    job = parsed["jobs"]["validate-and-dispatch"]
    dispatch_step = next(
        step for step in job["steps"] if step.get("name") == "Dispatch hermes-zh site content sync"
    )

    assert dispatch_step["env"]["TARGET_REPO"] == "zcweah1981/hermes-zh"
    assert dispatch_step["env"]["DISPATCH_EVENT_TYPE"] == "content-updated"
    assert "SITE_REPO_DISPATCH_TOKEN" in dispatch_step["env"]
    assert "secrets.SITE_REPO_DISPATCH_TOKEN" in str(dispatch_step["env"]["SITE_REPO_DISPATCH_TOKEN"])


def test_dispatch_authorization_header_uses_only_secret_env_var():
    body = workflow_text()

    assert "${SITE...EN}" not in body
    assert "Authorization: Bearer ${SITE_REPO_DISPATCH_TOKEN}" in body
    assert "::add-mask::${SITE_REPO_DISPATCH_TOKEN}" in body
    assert not re.search(r"Authorization:\s*Bearer\s+\$\{SITE\.\.\.EN\}", body)


def test_dispatch_payload_is_file_backed_and_contract_validated():
    body = workflow_text()

    assert "dispatch-payload.json" in body
    assert "--data-binary @dispatch-payload.json" in body
    assert '-d "${payload}"' not in body
    assert "re.fullmatch(r'[0-9a-f]{40}', sha)" in body
    assert "'event_type': os.environ['DISPATCH_EVENT_TYPE']" in body
    assert "payload['event_type'] != 'content-updated'" in body

    for key in [
        "content_repo",
        "content_ref",
        "content_sha",
        "actor",
        "run_id",
        "source_workflow_url",
    ]:
        assert key in body


def test_dispatch_curl_fails_clearly_and_summary_reports_audit_fields():
    body = workflow_text()

    assert "curl -sS -fL --retry 3 --retry-delay 2 -X POST" in body
    assert "https://api.github.com/repos/${TARGET_REPO}/dispatches" not in body
    assert "api_base=\"https://api.github.com\"" in body
    assert "dispatch_path=\"/repos/${TARGET_REPO}/dispatches\"" in body
    assert '"${api_base}${dispatch_path}"' in body
    assert "X-GitHub-Api-Version: 2022-11-28" in body

    for summary_line in [
        "target_repo: ${TARGET_REPO}",
        "event_type: ${DISPATCH_EVENT_TYPE}",
        "content_sha: ${GITHUB_SHA}",
        "content_ref: main",
    ]:
        assert summary_line in body
