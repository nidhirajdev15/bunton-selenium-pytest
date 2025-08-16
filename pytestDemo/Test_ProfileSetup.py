import time

import pytest

from pageObjects.pom_homepage import HomePage
from pageObjects.pom_profilesetup import ProfileSetup
from utilities import excelReader


@pytest.mark.usefixtures("invoke_browser_for_class")
class Test_ProfileSetup:

    excel_file_path = "C:\\Users\\nidhi.rajdev_infobea\\PycharmProjects\\SeleniumWithPython_Q1\\testData\\test_data.xlsx"

    def login_with_email(self):
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.login = self.home.click_login()
        self.login.enter_login_email(excelReader.readData(self.excel_file_path, "LoginData", 2, 1))
        self.login.enter_login_password(excelReader.readData(self.excel_file_path, "LoginData", 2, 2))
        self.login.click_login_submit()
        assert self.login.validate_login_success() is True
        self.driver.get("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/ProfileSetup")

    def test_add_education(self):
        self.login_with_email()
        self.profile_setup = ProfileSetup(self.driver, self.wait)
        self.profile_setup.click_education()
        self.profile_setup.add_save_education()
        self.profile_setup.validate_education_save_success()

    def test_add_work_experience(self):
        # self.login_with_email()
        self.profile_setup = ProfileSetup(self.driver, self.wait)
        self.profile_setup.click_work_experience()
        self.profile_setup.add_save_work_experience()
        self.profile_setup.validate_add_work_experience_success()

    def test_upload_resume(self):
        # self.login_with_email()
        self.profile_setup = ProfileSetup(self.driver, self.wait)
        self.profile_setup.click_upload_resume()
        self.profile_setup.upload_resume_file()
        self.profile_setup.click_upload_button()
        self.profile_setup.validate_resume_upload_success()

    def test_select_language(self):
        # self.login_with_email()
        self.profile_setup = ProfileSetup(self.driver, self.wait)
        self.profile_setup.click_languages()
        self.profile_setup.select_languages()
        self.profile_setup.save_languages()
        self.profile_setup.validate_select_languages_success()

    def test_select_avatar(self):
        # self.login_with_email()
        self.profile_setup = ProfileSetup(self.driver, self.wait)
        self.profile_setup.click_select_avatar()
        self.profile_setup.select_avatar()
        self.profile_setup.save_avatar()
        self.profile_setup.validate_save_avatar_success()

    def test_additional_infos(self):
        # self.login_with_email()
        self.profile_setup = ProfileSetup(self.driver, self.wait)
        self.profile_setup.click_additional_infos()
        self.profile_setup.enter_about_you()
        self.profile_setup.enter_your_profession()
        self.profile_setup.select_business_network()
        self.profile_setup.select_your_preferences()
        self.profile_setup.enter_linkedin_url()
        self.profile_setup.click_save_additional_infos()
        self.profile_setup.validate_additional_info_save_success()
