# To validate Forgot Password functionality
import time
from pageObjects.pom_homepage import HomePage


class Test_ForgotPassword:

    def test_forgot_password_valid_email(self, invoke_browser_for_function):
        self.driver, self.wait = invoke_browser_for_function
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.login = self.home.click_login()
        self.forgot_password = self.login.click_forgot_password()
        self.yopmail = self.forgot_password.enter_forgotpwd_email("charlie@yopmail.com")
        time.sleep(5)
        assert self.forgot_password.verify_email() is True
        self.reset_password = self.yopmail.fetch_verify_otp("charlie@yopmail.com")
        time.sleep(5)
        self.reset_password.verify_heading()
        self.reset_password.set_new_password("Test@12345")
        self.reset_password.click_submit()
        self.reset_password.verify_reset_password_success()

    def test_forgot_password_invalid_email(self, invoke_browser_for_function):
        self.driver, self.wait = invoke_browser_for_function
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.login = self.home.click_login()
        self.forgot_password = self.login.click_forgot_password()
        self.yopmail = self.forgot_password.enter_forgotpwd_email("nidhi321@yopmail.com")
        assert self.forgot_password.verify_email() is False
