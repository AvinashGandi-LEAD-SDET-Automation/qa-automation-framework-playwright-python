from pages.login_page import LoginPage
from pages.produtct_page import ProductPage
import time

# ----------------------------------------
# Test Case 1
# Verify user successfully logged in
# ----------------------------------------
def test_user_logged_in_successfully(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.navigate()
    login_page.login("visual_user", "secret_sauce")
    time.sleep(2)
    assert product_page.is_logged_in()


# ----------------------------------------
# Test Case 2
# Verify product list is displayed
# ----------------------------------------
def test_product_list_displayed(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    products = product_page.get_product_list()

    assert len(products) > 0


# ----------------------------------------
# Test Case 3
# Add specific product and verify cart count
# ----------------------------------------
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