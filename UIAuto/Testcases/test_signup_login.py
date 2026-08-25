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

from UIAuto.Pages.signupLoginPage import SignupLogin
from UIAuto.Pages.homepPage import HomePage


class TestSignupLogin:

    def test_do_signup(self, page):
        page = page
        signup_login = SignupLogin(page)
        home = HomePage(page)
        home.navigate("https://automationexercise.com/")
        assert home.locator_is_visible(home.home_icon), "Home page is not loading"
        home.click_signup()
        signup_login.do_signup("msn python", "msnpython@gmail.com")



