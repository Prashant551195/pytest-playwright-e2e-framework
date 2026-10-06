import allure
from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator(".cart_item")
        self.item_names = page.locator(".cart_item .inventory_item_name")
        self.checkout_button = page.locator("[data-test='checkout']")

    @allure.step("Click checkout")
    def checkout(self):
        self.checkout_button.click()