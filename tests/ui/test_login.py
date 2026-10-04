import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_valid_login(login_page, inventory_page, users):
    login_page.open()
    login_page.login(users["valid"]["username"], users["valid"]["password"])
    expect(inventory_page.title).to_have_text("Products")


@pytest.mark.smoke
def test_invalid_login(login_page, users):
    login_page.open()
    login_page.login(users["invalid"]["username"], users["invalid"]["password"])
    expect(login_page.error).to_contain_text(
        "Username and password do not match"
    )


@pytest.mark.smoke
def test_locked_out_user(login_page, users):
    login_page.open()
    login_page.login(users["locked"]["username"], users["locked"]["password"])
    expect(login_page.error).to_contain_text("locked out")