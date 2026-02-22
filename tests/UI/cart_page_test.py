from pages.login_page import LoginPage
from pages.produtct_page import ProductPage
from pages.cart_page import CartPage
import allure


@allure.feature("Cart Page Functionality")
@allure.story("Navigate to Cart Page")
@allure.severity(allure.severity_level.NORMAL)
def test_navigate_to_cart(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    product_page.add_product_to_cart("Sauce Labs Backpack")
    product_page.open_cart()

    assert cart_page.is_cart_page_displayed()


@allure.feature("Cart Page Functionality")
@allure.story("Verify Cart Items Count")
@allure.severity(allure.severity_level.NORMAL)
def test_cart_items_count(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    product_page.add_multiple_products_to_cart([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ])

    product_page.open_cart()

    cart_items = cart_page.get_cart_items_count()

    assert cart_items == 2


@allure.feature("Cart Page Functionality")
@allure.story("Checkout Navigation")
@allure.severity(allure.severity_level.NORMAL)
def test_checkout_navigation(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    product_page.add_product_to_cart("Sauce Labs Backpack")
    product_page.open_cart()

    cart_page.click_checkout()

    assert "checkout" in page.url