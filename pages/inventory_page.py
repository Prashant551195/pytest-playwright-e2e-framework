import allure
from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    @allure.step("Add '{item_name}' to the cart")
    def add_to_cart(self, item_name):
        slug = item_name.lower().replace(" ", "-")
        self.page.locator(f"[data-test='add-to-cart-{slug}']").click()

    @allure.step("Remove '{item_name}' from the cart")
    def remove_from_cart(self, item_name):
        slug = item_name.lower().replace(" ", "-")
        self.page.locator(f"[data-test='remove-{slug}']").click()

    @allure.step("Open the cart")
    def open_cart(self):
        self.cart_link.click()