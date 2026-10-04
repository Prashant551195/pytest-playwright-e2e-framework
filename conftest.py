import json
from pathlib import Path

import pytest
from faker import Faker

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


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