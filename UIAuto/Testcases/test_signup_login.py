"""
as per the pytest convention test file name, test class name and
test defination name must be starts with test

fixtues: we can write setup and teardown in fixtures
ex: opening browser is setup and closing the browser at the end is teardown
scopes: function, class, module, session, package
by default is the function scope

assert: we can use to verification.

pytest testpath -s -v
-s: to display the logs in console
-v: verbose to get detailed information
-k: to collect the test case with testcase name
-m: to collect the testcases with marker name
-n: to run the testcases parallel

"""
import random
import string

from UIAuto.Pages.signupLoginPage import SignupLogin
from UIAuto.Pages.homepPage import HomePage


class TestSignupLogin:

    def test_do_signup(self, page):
        auto = random.choices(string.ascii_lowercase, k=8)
        email = "".join(auto)+"_msnpython@gmail.com"
        page = page
        signup_login = SignupLogin(page)
        home = HomePage(page)
        home.navigate("https://automationexercise.com/")
        assert home.locator_is_visible(home.home_icon), "Home page is not loading"
        home.click_signup()
        signup_login.do_signup("msn python", email)
        assert home.page.get_by_text(signup_login.enter_acct_info).is_visible(), "Signup is not loaded"
        signup_login.fill_signup_account_info_form('Mr', 'msn2121')
        signup_login.fill_signup_address_info("msn", "python", "msnpython", "Bangalore",
                                              "Marathalli", "Bangalore", "KA", "560037",
                                              "7799884799")
        assert signup_login.click_create_button_verify_account_creation(), "account creation is failed"


"""
windows / tabs
frames
alerts
file upload
shadow dom
"""

