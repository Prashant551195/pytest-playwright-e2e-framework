import json
import os
from pathlib import Path

import allure
import pytest
from faker import Faker

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.github_issue import create_issue


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


@pytest.fixture(scope="session")
def users():
    path = Path(__file__).parent / "data" / "users.json"
    with open(path) as f:
        return json.load(f)


@pytest.fixture
def checkout_data():
    fake = Faker()
    return {
        "first": fake.first_name(),
        "last": fake.last_name(),
        "zip": fake.postcode(),
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    page = item.funcargs.get("page")
    if page is not None:
        try:
            allure.attach(
                page.screenshot(),
                name="failure-screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:
            pass

    if os.getenv("CREATE_GITHUB_ISSUES", "false").lower() == "true":
        title = f"Test failed: {item.nodeid}"
        body = (
            "Automated test failure.\n\n"
            f"**Test:** `{item.nodeid}`\n\n"
            f"**Error (last lines):**\n```\n{str(report.longrepr)[-1500:]}\n```"
        )
        create_issue(title, body)