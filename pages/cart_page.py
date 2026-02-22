from playwright.sync_api import Page
import allure


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
        with allure.step("Checking if cart page is displayed"):
            return self.cart_title.is_visible()

    def get_cart_items_count(self):
        with allure.step("Getting count of items in cart"):
            return self.cart_items.count()

    # ---------- Actions ----------

    def click_checkout(self):
        with allure.step("Clicking checkout button"):
            self.checkout_button.click()

    def continue_shopping(self):
        with allure.step("Clicking continue shopping button"):
            self.continue_shopping_button.click()

    