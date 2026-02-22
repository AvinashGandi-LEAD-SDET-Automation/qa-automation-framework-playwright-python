import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def pw_instance():
    with sync_playwright() as pw:
        yield pw

@pytest.fixture(scope="session")
def browser(pw_instance):
   # browser = pw_instance.chromium.launch(headless=False, args=["--start-maximized"])
    browser = pw_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(viewport=None)
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()