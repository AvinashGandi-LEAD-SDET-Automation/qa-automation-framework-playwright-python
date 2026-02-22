from pages.login_page import LoginPage
from pages.product_page import ProductsPage



def test_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate()
    assert login_page.get_title() == "Swag Labs"
    login_page.login("standard_user","secret_sauce")
    login_page.get_title() == "Swag Labs"
    assert ProductsPage.is_logged_in() == True


def test_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate()
    assert login_page.get_title() == "Swag Labs"
    login_page.login("standard_user","invaldi_secret_sauce")
    login_page.get_title() == "Swag Labs"
    assert login_page.loginerror_message.is_visible() == True
    assert login_page.loginerror_message.text_content() == "Epic sadface: Username and password do not match any user in this service"
    
