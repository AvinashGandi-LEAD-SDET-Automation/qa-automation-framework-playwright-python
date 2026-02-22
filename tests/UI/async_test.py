from pages.login_page import LoginPage
from pages.produtct_page import ProductPage

# --------------------------------------------------
# Test 1
# Wait for element to become visible after login
# --------------------------------------------------
def test_wait_for_products_page_load(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Explicit wait for Products title
    product_page.products_title.wait_for(state="visible")

    assert product_page.products_title.is_visible()

# --------------------------------------------------
# Test 2
# Wait for dynamic UI update (cart badge)
# --------------------------------------------------
def test_cart_badge_wait(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    product_page.add_product_to_cart("Sauce Labs Backpack")

    # Wait until cart badge becomes visible
    product_page.cart_badge.wait_for(state="visible")

    cart_count = product_page.get_cart_count()

    assert cart_count == 1


# --------------------------------------------------
# Test 3
# Auto wait during navigation after click
# --------------------------------------------------
def test_navigation_auto_wait(page):

    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    product_page.open_cart()

    # Wait for URL change
    page.wait_for_url("**/cart.html")

    assert "cart" in page.url