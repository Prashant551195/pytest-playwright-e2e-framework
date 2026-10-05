import pytest
from playwright.sync_api import expect

from config.settings import API_BASE_URL, SAUCE_USER, SAUCE_PASSWORD
from utils.data_factory import build_booking


@pytest.fixture
def api_context(playwright):
    context = playwright.request.new_context(
        base_url=API_BASE_URL,
        extra_http_headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    yield context
    context.dispose()


@pytest.fixture
def booking(api_context):
    response = api_context.post("/booking", data=build_booking())
    assert response.ok
    body = response.json()
    return {"id": body["bookingid"], **body["booking"]}


@pytest.mark.e2e
def test_api_data_used_in_ui_checkout(
    login_page,
    inventory_page,
    cart_page,
    checkout_page,
    api_context,
    booking,
):
    # 1. Data was created through the API (see the booking fixture)
    # 2. Use that data in the UI checkout
    login_page.open()
    login_page.login(SAUCE_USER, SAUCE_PASSWORD)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    cart_page.checkout()
    checkout_page.fill_details(booking["firstname"], booking["lastname"], "411001")
    checkout_page.finish()
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")

    # 3. Verify the backend record again through the API
    response = api_context.get(f"/booking/{booking['id']}")
    assert response.ok
    assert response.json()["firstname"] == booking["firstname"]