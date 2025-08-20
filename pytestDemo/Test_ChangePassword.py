# To validate the change password functionality
import pytest
import allure

from pageObjects.pom_changepassword import ChangePassword
from pageObjects.pom_homepage import HomePage
from pageObjects.pom_profile import Profile


@pytest.mark.usefixtures("invoke_browser_for_class")
class Test_ChangePassword:

    @allure.title("Change Password")
    def test_change_password_with_valid_current_password(self):
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.loginPage = self.home.click_login()
        self.loginPage.enter_login_email("carol@yopmail.com")
        self.loginPage.enter_login_password("Test@1234")
        self.loginPage.click_login_submit()
        assert self.loginPage.validate_login_success() is True
        self.profile = Profile(self.driver, self.wait)
        self.profile.click_profile_icon()
        self.profile.click_settings()
        self.change_password = ChangePassword(self.driver, self.wait)
        self.change_password.set_current_password("Test@1234")
        self.change_password.set_new_password("Test@12345")
        self.change_password.click_submit()
        assert self.change_password.validate_change_password_success() is True

    def test_change_password_with_invalid_current_password(self):
        self.profile.click_profile_icon()
        self.profile.click_settings()
        self.change_password.set_current_password("Test@1234")
        self.change_password.set_new_password("Test@4321")
        self.change_password.click_submit()
        assert self.change_password.validate_change_password_success() is False
