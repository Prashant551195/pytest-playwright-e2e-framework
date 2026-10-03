import re
from playwright.sync_api import Page, expect

def test_saucedemo_title(page: Page):
    page.goto("https://www.saucedemo.com")
    expect(page).to_have_title(re.compile("Swag Labs"))