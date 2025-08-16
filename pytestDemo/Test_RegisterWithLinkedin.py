# To validate registration with LinkedIn

from pageObjects.pom_homepage import HomePage
from pageObjects.pom_onlinesurvey import OnlineSurvey


class Test_RegisterWithLinkedin:
    def test_register_with_linkedin(self, invoke_browser_for_function):
        self.driver, self.wait = invoke_browser_for_function
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.register = self.home.click_register()
        self.register.answer_registration_questions("TestName")
        self.register.click_register_with_linkedin()
        self.register.enter_linkedin_email_password("ibqa12@gmail.com", "InfoBile@191")
        self.register.click_linkedin_signin()
        self.survey = OnlineSurvey(self.driver, self.wait)
        assert self.survey.validate_survey_popup_appearance() is True
