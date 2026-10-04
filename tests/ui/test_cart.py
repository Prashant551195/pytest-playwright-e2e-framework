import pytest
from playwright.sync_api import expect


@pytest.fixture
def logged_in(login_page, users):
    login_page.open()
    login_page.login(users["valid"]["username"], users["valid"]["password"])


@pytest.mark.regression
def test_add_item_shows_badge(logged_in, inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")


@pytest.mark.regression
def test_add_two_items(logged_in, inventory_page, cart_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bike Light")
    inventory_page.open_cart()
    expect(cart_page.items).to_have_count(2)


@pytest.mark.regression
def test_remove_item(logged_in, inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.remove_from_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_count(0)