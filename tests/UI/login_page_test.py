import pytest
from pages.login_page import LoginPage
import time


def test_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate()
    assert login_page.get_title() == "Swag Labs"
    login_page.login("standard_user","secret_sauce")
    login_page.get_title() == "Swag Labs"
    time.sleep(5)
