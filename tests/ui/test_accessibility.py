import json

import allure
import pytest
from axe_playwright_python.sync_playwright import Axe


@pytest.mark.a11y
def test_login_page_has_no_critical_violations(page, login_page):
    login_page.open()
    results = Axe().run(page)
    violations = results.response["violations"]

    allure.attach(
        json.dumps(violations, indent=2),
        name="axe-violations",
        attachment_type=allure.attachment_type.JSON,
    )

    critical = [v for v in violations if v.get("impact") == "critical"]
    print(f"Total violations: {results.violations_count}, critical: {len(critical)}")
    assert not critical, [v["id"] for v in critical]