import pytest
from playwright.sync_api import expect


@pytest.mark.e2e
def test_complete_purchase(
    login_page,
    inventory_page,
    cart_page,
    checkout_page,
    users,
    checkout_data,
):
    login_page.open()
    login_page.login(users["valid"]["username"], users["valid"]["password"])

    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    expect(cart_page.items).to_have_count(1)

    cart_page.checkout()
    checkout_page.fill_details(
        checkout_data["first"],
        checkout_data["last"],
        checkout_data["zip"],
    )
    checkout_page.finish()

    expect(checkout_page.complete_header).to_have_text(
        "Thank you for your order!"
    )