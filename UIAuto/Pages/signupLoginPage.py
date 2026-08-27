# from basepage import BasePage
from UIAuto.Pages.basepage import BasePage


class SignupLogin(BasePage):
    # We can write all the locators and methods for signup and login features

    signup_login_link = '[href="/login"]'
    new_user_signup = 'New User Signup!'
    name = '[data-qa="signup-name"]'
    email = '[data-qa="signup-email"]'
    submit_btn = '[data-qa="signup-button"]'

    # account information
    enter_acct_info = 'Enter Account Information'
    mr_btn = '[id="id_gender1"]'
    mrs_btn = '[id="id_gender2"]'
    password_field = '[name="password"]'
    days_dp = '[id="days"]'
    months_dp = '[id="months"]'
    years_dp = '[id="years"]'
    news_letter_check = '[id="newsletter"]'
    receive_options_check = '[id="optin"]'

    # address information
    first_name = '[id="first_name"]'
    last_name = '[id="last_name"]'
    company = '[id="company"]'
    address = '[id="address1"]'
    address2 = '[id="address2"]'
    state = '[id="state"]'
    city = '[id="city"]'
    zipcode = '[id="zipcode"]'
    mobile = '[id="mobile_number"]'
    create_account = '[data-qa="create-account"]'

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

    def fill_signup_address_info(self, first_name, last_name, company, address1, address2, city,
                                 state, zipcode, mobile):
        print("****** fill signup address info started ******")
        self.fill(self.first_name, first_name)
        self.fill(self.last_name, last_name)
        self.fill(self.company, company)
        self.fill(self.address, address1)
        self.fill(self.address2, address2)
        self.fill(self.state, state)
        self.fill(self.city, city)
        self.fill(self.zipcode, zipcode)
        self.fill(self.mobile, mobile)
        print("**** fill signuo address info ended ********")

    def click_create_button_verify_account_creation(self):
        """
        This will click the create account button and will return account created status
        :return: boolean
        """
        print("**** create account verification started *****")
        self.click(self.create_account)
        return self.page.get_by_text('ACCOUNT CREATED').is_visible()
