from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        # Cart page title
        self.cart_title = page.locator(".title")

        # Cart items
        self.cart_items = page.locator(".cart_item")

        # Checkout button
        self.checkout_button = page.locator("#checkout")

        # Continue shopping button
        self.continue_shopping_button = page.locator("#continue-shopping")

    # ---------- Validations ----------

    def is_cart_page_displayed(self):
        return self.cart_title.is_visible()

    def get_cart_items_count(self):
        return self.cart_items.count()

    # ---------- Actions ----------

    def click_checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()