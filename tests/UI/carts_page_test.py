import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


USERNAME = "standard_user"
PASSWORD = "secret_sauce"


# -------------------------------------------------------
# Validate cart contains correct products
# -------------------------------------------------------
def test_cart_contains_selected_products(page):

    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    login.navigate()
    login.login(USERNAME, PASSWORD)

    expected_products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ]

    for product in expected_products:
        products.add_product_to_cart(product)

    cart.open()

    cart_items = cart.get_cart_items()
    cart_names = [item["name"] for item in cart_items]

    assert set(cart_names) == set(expected_products)


# -------------------------------------------------------
# Validate cart total equals sum of item prices
# -------------------------------------------------------
def test_cart_total_matches_item_prices(page):

    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    login.navigate()
    login.login(USERNAME, PASSWORD)

    products.add_product_to_cart("Sauce Labs Backpack")
    products.add_product_to_cart("Sauce Labs Bike Light")

    cart.open()

    items = cart.get_cart_items()

    expected_total = sum(item["price"] for item in items)
    actual_total = cart.get_cart_total()

    assert expected_total == actual_total


# -------------------------------------------------------
# Validate cart empty immediately after login
# -------------------------------------------------------
def test_cart_is_empty_after_login(page):

    login = LoginPage(page)
    cart = CartPage(page)

    login.navigate()
    login.login(USERNAME, PASSWORD)

    cart.open()

    assert len(cart.get_cart_items()) == 0