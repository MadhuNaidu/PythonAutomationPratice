from UIAuto.Pages.basepage import BasePage


class HomePage(BasePage):

    home_icon = '[class="fa fa-home"]'
    products_link = '[href="/products"]'
    carts_link = '[href="/view_cart"]'
    signup_login_link = '[href="/login"]'

    def launch_url(self, url):
        self.navigate(url)

    def locator_is_visible(self, locator, timeout=30000):
        return self.is_visible(locator, timeout)

    def click_signup(self):
        self.click(self.signup_login_link)




