from pages.login_page import LoginPage
from pages.produtct_page import ProductPage
import time



def test_login_page(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    login_page.navigate()
    assert login_page.get_title() == "Swag Labs"
    login_page.login("visual_user","secret_sauce")
    time.sleep(1)
    login_page.get_title() == "Swag Labs"
    #product_page.inventory_items.is_visible() == True
 


def test_login_pageerror(page):
    login_page = LoginPage(page)
    login_page.navigate()
    assert login_page.get_title() == "Swag Labs"
    login_page.login("visual_user","secret_sauce_invalid")
    login_page.get_title() == "Swag Labs"
    time.sleep(1)
    login_page.loginerror_message.is_visible() == True
    #assert login_page.loginerror_message.is_visible() == True
    #assert login_page.loginerror_message.text_content() == "Epic sadface: Username and password do not match any user in this service"
    
