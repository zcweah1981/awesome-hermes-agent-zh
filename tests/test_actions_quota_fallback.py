from pathlib import Path


REPO = Path(__file__).resolve().parents[1]


def test_local_verification_exists_for_actions_quota_exhaustion():
    script = REPO / "scripts" / "verify-local.ps1"
    docs = (REPO / "docs" / "ci.md").read_text(encoding="utf-8")

    assert script.exists()
    body = script.read_text(encoding="utf-8")
    assert "python -m pytest -q" in body
    assert "normalize_route_order.py" in body
    assert "content_quality_check.py" in body
    assert "Actions 额度耗尽" in docs
    assert "verify-local.ps1" in docs
