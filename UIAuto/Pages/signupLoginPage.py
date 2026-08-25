# from basepage import BasePage
from UIAuto.Pages.basepage import BasePage

class SignupLogin(BasePage):
    # We can write all the locators and methods for signup and login features

    signup_login_link = '[href="/login"]'
    new_user_signup = 'New User Signup!'
    name = '[data-qa="signup-name"]'
    email = '[data-qa="signup-email"]'
    submit_btn = '[data-qa="signup-button"]'

    def enter_username(self, username):
        self.fill(self.name, username)

    def enter_email(self, email):
        self.fill(self.email, email)

    def click_login(self):
        self.click(self.submit_btn)

    def do_signup(self, username, email):
        print("******** do login started *********")
        self.enter_username(username)
        self.enter_email(email)
        self.click_login()
        print("******** do login ended *********")

