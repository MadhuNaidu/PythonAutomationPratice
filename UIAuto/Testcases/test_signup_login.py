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
import json
import time

import pytest
from UIAuto.Pages.signupLoginPage import SignupLogin
from UIAuto.Pages.homepPage import HomePage


class TestSignupLogin:

    def handle_dialog(dialog):
        message = dialog.message
        print(f"Message: {message}")
        dialog.accept()

    def handle_filedownload(download):
        file_path = './test.zip'
        # download.save_as(file_path)
        download.save_as('./test.zip')

    with open(r"C:\Users\madhusudhana_naidu\PycharmProjects\AutoExPw\UIAuto\Testdata\user_creation_data.json") as file:
        test_data = json.load(file)

    @pytest.mark.user_reg
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", test_data)
    def test_do_signup(self, page, data):
        auto = random.choices(string.ascii_lowercase, k=8)
        email = "".join(auto)+"_"+data["email"]
        name = "".join(auto)+" "+data["name"]
        print(f"name: {name} and email: {email}")
        page = page
        signup_login = SignupLogin(page)
        home = HomePage(page)
        home.navigate("https://automationexercise.com/")
        assert home.locator_is_visible(home.home_icon), "Home page is not loading"
        home.click_signup()
        signup_login.do_signup(name, email)
        assert home.page.get_by_text(signup_login.enter_acct_info).is_visible(), "Signup is not loaded"
        signup_login.fill_signup_account_info_form('Mr', 'msn2121')
        signup_login.fill_signup_address_info("msn", "python", "msnpython", "Bangalore",
                                              "Marathalli", "Bangalore", "KA", "560037",
                                              "7799884799")
        assert signup_login.click_create_button_verify_account_creation(), "account creation is failed"

    @pytest.mark.smoke
    @pytest.mark.alert
    def test_alerts(self, page):
        """
        Handling the alerts with dialog
        """
        # try:
        #     page.locator('[href="#OKTab"]').click()
        #     page.wait_for_timeout(2000)
        #     with page.expect_event("dialog") as d:
        #         page.locator('[onclick="alertbox()"]').click()
        #     page.wait_for_timeout(2000)
        #     dialog = d.value
        #     print(d.message)
        #     print(d.type)
        #     dialog.accept()
        # except Exception as e:
        #     print("Got the execpetion", e)
        # ok and cancel
        try:
            page.locator('[href="#CancelTab"]').click()
            page.wait_for_timeout(2000)
            with page.expect_event("dialog") as d:
                page.locator('[onclick="confirmbox()"]').click()

            page.wait_for_timeout(2000)
            dialog = d.value
            print(dialog.type)
            print(dialog.message)
            dialog.accept()
        except Exception as e:
            print(f"exception: {e}")
        page.locator('[href="#Textbox"]').click()
        page.wait_for_timeout(2000)
        with page.expect_event('dialog') as d:
            page.locator('[onclick="promptbox()"]').click()
        page.wait_for_timeout(2000)
        dialog = d.value
        dialog.accept("hello")
        """
        page.locator('[href="#CancelTab"]').click()
        page.wait_for_timeout(2000)
        page.on("dialog", handle_dialog)
        # once, on
        page.wait_for_selector('//div[@id="CancelTab"]/button').click()
        page.wait_for_timeout(2000)
        """

    @pytest.mark.default_aleart
    def test_alerts_default(self, page):

        page.locator('[href="#CancelTab"]').click()
        page.wait_for_timeout(2000)
        page.locator('[onclick="confirmbox()"]').click()
        page.wait_for_timeout(2000)
        time.sleep(10)

    @pytest.mark.windows
    def test_windows_pages(self, page):
        page = page
        page.locator('[href="#Tabbed"]').click()
        page.locator('[href="http://www.selenium.dev"]').click()
        print(page.title())
        page.context.pages[1].bring_to_front()

    @pytest.mark.frame
    def test_iframes(self, page):
        page = page
        page.locator('[href="#Single"]').click()
        frame = page.frame_locator('[id="singleframe"]')
        frame.get_by_text('iFrame Demo')
        frame.locator('[type="text"]').fill("hello hai")

        # nested frames
        frame1 = page.frame_locator('[src="MultipleFrames.html"]')
        print(frame1.get_by_text('Nested iFrames').text_content())
        frame2 = frame1.frame_locator('[src="SingleFrame.html"]')
        frame2.locator('[type="text"]').fill("msn python")

    @pytest.mark.fileupload
    def test_file_upload(self, page):
        page.goto('https://demo.automationtesting.in/FileUpload.html')

        # single file upload
        page.query_selector('[id="input-4"]').set_input_files(r'C:\Users\madhusudhana_naidu\PycharmProjects\PWAuto\uft_new.png')
        # upload multiple files
        page.query_selector('[id="input-4"]').set_input_files(
            [r'C:\Users\madhusudhana_naidu\PycharmProjects\PWAuto\uft_new.png',
             r"C:\Users\madhusudhana_naidu\Desktop\Profile.png"])
        page.wait_for_timeout(2000)

    @pytest.mark.filedownload
    def test_file_download(self, page):
        page.goto('https://demo.automationtesting.in/FileDownload.html')
        page.wait_for_selector('[id="textbox"]').fill('hello this is file download example')
        page.wait_for_selector('[id="createTxt"]').click()
        # page.on('download', self.handle_filedownload)
        # page.wait_for_selector('[id="link-to-download"]').click()
        with page.expect_download() as d:
            page.wait_for_selector('[id="link-to-download"]').click()
        download_info = d.value
        download_info.save_as("test_one.zip")
        # page.query_selector('[id="input-4"]').set_input_files(
        #     r'C:\Users\madhusudhana_naidu\PycharmProjects\PWAuto\uft_new.png')
        page.wait_for_timeout(2000)


"""
alerts / popup / dialog
windows / tabs
frames
file upload / download

shadow dom: 


file upload / download
storage state
action chains
screenshots / videos
Authentication & Storage State
"""

