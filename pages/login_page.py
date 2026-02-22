from playwright.sync_api import expect
import allure

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.loginerror_message = page.locator(".error-button")

    def navigate(self):
        with allure.step("Navigating to the login page"):
            self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        with allure.step(f"Logging in with username: {username} and password: {password}"):
            self.username_input.fill(username)
            self.password_input.fill(password)
        with allure.step("Clicking login button"):
            self.login_button.click()
      #  expect(self.page.locator(".inventory_list")).to_be_visible()
    
    def get_title(self):
        return self.page.title()