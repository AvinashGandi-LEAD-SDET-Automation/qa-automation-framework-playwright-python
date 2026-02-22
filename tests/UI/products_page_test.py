import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


USERNAME = "standard_user"
PASSWORD = "secret_sauce"


# -------------------------------------------------------
# Validate cart badge updates after adding products
# -------------------------------------------------------
def test_cart_badge_updates_after_adding_products(page):

    login = LoginPage(page)
    products = ProductsPage(page)

    login.navigate()
    login.login(USERNAME, PASSWORD)

    products.add_product_to_cart("Sauce Labs Backpack")
    products.add_product_to_cart("Sauce Labs Bike Light")

    assert products.get_cart_count() == 2


# -------------------------------------------------------
# Validate cart badge count matches cart items
# -------------------------------------------------------
def test_cart_badge_matches_cart_items(page):

    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    login.navigate()
    login.login(USERNAME, PASSWORD)

    products.add_product_to_cart("Sauce Labs Backpack")
    products.add_product_to_cart("Sauce Labs Bike Light")

    badge_count = products.get_cart_count()

    cart.open()
    cart_items = cart.get_cart_items()

    assert badge_count == len(cart_items)