"""
We are going to write all the methods on top off selenium / playwright
"""
"""
Playwright: it is open source to perform ui, api and mobile automation.
it is developed by microsoft.

Page: fixture
pom:
basepage will contain generic methods that we can use in other classes.
navigate, click, fill, select_options
"""

from playwright.sync_api import Page


class BasePage:

    # pep8 standards
    def __init__(self, page: Page): # constructor
        self.page = page # instance attribute

    def navigate(self, url):
        self.page.goto(url, timeout=60000)

    def click(self, locator):
        try:
            self.page.click(locator)
        except TimeoutError as e:
            print(f"Got the exception: {e}")

    def fill(self, locator, text):
        try:
            self.page.fill(locator, text)
        except TimeoutError as e:
            print(f"Got the exception: {e}")

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible(timeout=30000)

    def is_checked(self, locator):
        return self.page.locator(locator).is_checked()

