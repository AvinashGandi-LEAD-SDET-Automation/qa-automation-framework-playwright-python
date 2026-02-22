from pages.login_page import LoginPage
from pages.produtct_page import ProductPage
import time
import allure

@allure.feature("Product Page Functionality")
@allure.story("Verify user is logged in successfully")
@allure.severity(allure.severity_level.NORMAL)
def test_user_logged_in_successfully(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.navigate()
    login_page.login("visual_user", "secret_sauce")
    time.sleep(2)
    assert product_page.is_logged_in()


@allure.feature("Product Page Functionality")
@allure.story("Verify product list is displayed")
@allure.severity(allure.severity_level.NORMAL)
def test_product_list_displayed(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    products = product_page.get_product_list()

    assert len(products) > 0


@allure.feature("Product Page Functionality")
@allure.story("Add specific product to cart and validate cart count")
@allure.severity(allure.severity_level.NORMAL)
def test_add_specific_product_to_cart(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    product_page.add_product_to_cart("Sauce Labs Backpack")
    product_page.add_product_to_cart("Sauce Labs Bike Light")
    cart_count = product_page.get_cart_count()
    time.sleep(3)
    assert cart_count == 2

@allure.feature("Product Page Functionality")
@allure.story("Add specific product to cart and fail cart count validation")
@allure.severity(allure.severity_level.NORMAL)
def test_add_specific_product_to_cart_truefail(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    product_page.add_product_to_cart("Sauce Labs Backpack")
    product_page.add_product_to_cart("Sauce Labs Bike Light")
    cart_count = product_page.get_cart_count()
    time.sleep(3)
    assert cart_count == 4