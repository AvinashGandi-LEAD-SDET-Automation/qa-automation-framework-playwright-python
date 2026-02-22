from pages.login_page import LoginPage
from pages.produtct_page import ProductPage
import time
import allure

# @allure.feature("Login Functionality")
# @allure.story("User Login")
# class LoginPageTest:

#     @allure.title("Verify user can login successfully with valid credentials")
#     @allure.severity(allure.severity_level.NORMAL)

@allure.feature("Login Functionality")
@allure.story("Valid user Login")
@allure.severity(allure.severity_level.NORMAL)
def test_login_page(page):
        login_page = LoginPage(page)
        product_page = ProductPage(page)
        login_page.navigate()
        assert login_page.get_title() == "Swag Labs"
        login_page.login("visual_user","secret_sauce")
        login_page.get_title() == "Swag Labs"
       
    

@allure.feature("Login Functionality")
@allure.story("Invalid user Login")
@allure.severity(allure.severity_level.NORMAL)
def test_login_pageerror(page):
        login_page = LoginPage(page)
        login_page.navigate()
        assert login_page.get_title() == "Swag Labs"
        login_page.login("visual_user","secret_sauce_invalid")
        login_page.get_title() == "Swag Labs"
        login_page.loginerror_message.is_visible() == True


@allure.feature("Login Functionality")
@allure.story("Failed Valid user Login")
@allure.severity(allure.severity_level.NORMAL)
def test_login_page_failed(page):
        login_page = LoginPage(page)
        product_page = ProductPage(page)
        login_page.navigate()
        assert login_page.get_title() == "Swag Labs"
        login_page.login("visual_user","wrong_password")
        login_page.get_title() == "Swag Labs"
        assert login_page.loginerror_message.is_visible() == False
        
        
