from scripts.content_quality_check import BASELINE, collect_issues, validate_image_formats

import yaml


def test_content_quality_debt_does_not_exceed_reviewed_baseline():
    validate_image_formats()
    baseline = yaml.safe_load(BASELINE.read_text(encoding="utf-8"))
    issues = collect_issues()

    for key, values in issues.items():
        assert set(values) <= set(baseline.get(key, []))
