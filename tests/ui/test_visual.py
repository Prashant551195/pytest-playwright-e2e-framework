import pytest

from utils.visual import assert_matches_baseline


@pytest.mark.visual
def test_login_page_looks_the_same(page, login_page, browser_name):
    page.set_viewport_size({"width": 1280, "height": 720})
    login_page.open()
    page.wait_for_load_state("networkidle")
    assert_matches_baseline(page.screenshot(), f"login_page_{browser_name}")