import pytest
from playwright.sync_api import expect
from config.settings import SAUCE_USER, SAUCE_PASSWORD


@pytest.mark.smoke
def test_add_item_to_cart(login_page, inventory_page, cart_page):
    login_page.open()
    login_page.login(SAUCE_USER, SAUCE_PASSWORD)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    expect(cart_page.item_names).to_have_text("Sauce Labs Backpack")