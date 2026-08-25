"""
We are going to write all the methods on top off selenium / playwright

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

    def select_dropdown_option(self, dropdown_locator, dropdown_value, dropdown_value_type):
        """
        This method will select the dropdown option from the dropdown
        :param dropdown_locator: it is a web element for dropdown item
        :param dropdown_value: dropdown value to select the dropdown option, ex: label, index, value
        :param dropdown_value_type: it is a dropdown value type, ex: label, index, value type
        """
        dropdown = self.page.locator(dropdown_locator)
        if dropdown_value_type == 'label':
            dropdown.select_option(label=dropdown_value)
        elif dropdown_value_type == 'value':
            dropdown.select_option(value=dropdown_value)
        else:
            dropdown.select_option(index=dropdown_value)

    def is_visible(self, locator, timeout):
        return self.page.locator(locator).is_visible(timeout=timeout)

    def is_checked(self, locator):
        return self.page.locator(locator).is_checked()

    def check_checkbox(self, locator):
        if self.is_checked(locator):
            print("already checkbox is checked")
        else:
            print("select check box")
            self.page.locator(locator).click()

