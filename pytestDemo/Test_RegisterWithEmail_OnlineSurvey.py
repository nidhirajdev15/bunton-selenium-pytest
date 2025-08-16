# To test registration with email and validate online survey link navigation
import time

import pytest
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_homepage import HomePage
from pageObjects.pom_onlinesurvey import OnlineSurvey
from pageObjects.pom_profilesetup import ProfileSetup
from pageObjects.pom_yopmail import Yopmail
from utilities import excelReader


@pytest.mark.usefixtures("invoke_browser_for_class")
class Test_RegisterWithEmail_OnlineSurvey:
    excel_file_path = "C:\\Users\\nidhi.rajdev_infobea\\PycharmProjects\\SeleniumWithPython_Q1\\testData\\test_data.xlsx"

    def test_register_with_email(self):
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.registration = self.home.click_register()
        assert self.wait.until(expected_conditions.url_contains("/registration"))
        name = excelReader.readData(self.excel_file_path, "RegistrationData", 2, 1)
        self.registration.answer_registration_questions(name)
        self.registration.click_register_with_email()
        email = excelReader.readData(self.excel_file_path, "RegistrationData", 2, 7)
        password = excelReader.readData(self.excel_file_path, "RegistrationData", 2, 8)
        self.registration.enter_email_password(email, password)
        self.registration.click_accept_terms()
        self.registration.click_submit()
        if self.registration.verify_registration_success():
            self.yopmail = Yopmail(self.driver, self.wait)
            time.sleep(5)
            self.yopmail.fetch_verify_otp(email)
            self.registration.verify_otp_success()

    def test_click_survey_link(self):
        self.survey = OnlineSurvey(self.driver, self.wait)
        self.survey.validate_survey_popup_appearance()
        self.survey.click_survey_button()
        self.driver.switch_to.window(self.driver.window_handles[0])
