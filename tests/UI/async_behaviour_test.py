import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage



USERNAME = "standard_user"
PASSWORD = "secret_sauce"


# -------------------------------------------------------
# Validate async UI update using Playwright waits
# -------------------------------------------------------
def test_add_to_cart_wait_behavior(page):

    login = LoginPage(page)
    products = ProductsPage(page)

    login.navigate()
    login.login(USERNAME, PASSWORD)

    product_name = "Sauce Labs Backpack"

    products.add_product_to_cart(product_name)

    # ✅ Playwright explicit wait
    cart_badge = page.locator(".shopping_cart_badge")

    # waits automatically until visible
    expect(cart_badge).to_be_visible()

    # waits until correct value appears
    expect(cart_badge).to_have_text("1")