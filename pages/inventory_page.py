from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_to_cart(self, item_name):
        slug = item_name.lower().replace(" ", "-")
        self.page.locator(f"[data-test='add-to-cart-{slug}']").click()

    def remove_from_cart(self, item_name):
        slug = item_name.lower().replace(" ", "-")
        self.page.locator(f"[data-test='remove-{slug}']").click()

    def open_cart(self):
        self.cart_link.click()