# from basepage import BasePage
from UIAuto.Pages.basepage import BasePage


class SignupLogin(BasePage):
    # We can write all the locators and methods for signup and login features

    signup_login_link = '[href="/login"]'
    new_user_signup = 'New User Signup!'
    name = '[data-qa="signup-name"]'
    email = '[data-qa="signup-email"]'
    submit_btn = '[data-qa="signup-button"]'
    enter_acct_info = 'Enter Account Information'
    mr_btn = '[id="id_gender1"]'
    mrs_btn = '[id="id_gender2"]'
    password_field = '[name="password"]'
    days_dp = '[id="days"]'
    months_dp = '[id="months"]'
    years_dp = '[id="years"]'
    news_letter_check = '[id="newsletter"]'
    receive_options_check = '[id="optin"]'

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

    def fill_signup_account_info_form(self, title, password):
        #  Fill details: Title Password, Date of birth
        print("******** fill signup form started ********")
        if title == 'Mr':
            self.click(self.mr_btn)
        else:
            self.click(self.mrs_btn)
        self.fill(self.password_field, password)
        self.select_dropdown_option(self.days_dp, '10', 'value')
        self.select_dropdown_option(self.months_dp, 'August', 'label')
        self.select_dropdown_option(self.years_dp, dropdown_value='1996', dropdown_value_type='value')
        self.check_checkbox(self.news_letter_check)
        self.check_checkbox(self.receive_options_check)
        print("******** fill signup form is ended *******")
    def fill_signup_address_info(self, first_name, last_name, company, address1, address2, country,
                          state, zipcode, mobile):
        pass
