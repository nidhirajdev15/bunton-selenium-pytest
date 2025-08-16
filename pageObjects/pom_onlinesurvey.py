import time

from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions


class OnlineSurvey:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.survey_popup_text = (By.XPATH, "//h6[contains(text(),'Was braucht es')]")
        self.survey_button = (By.XPATH, "//h3[contains(text(),'zur Online Umfrage')]")
        self.survey_close_button = (By.CSS_SELECTOR, "svg[data-testid='CloseIcon']")

    def validate_survey_popup_appearance(self):
        try:
            time.sleep(10)
            survey_popup = self.wait.until(expected_conditions.visibility_of_element_located(self.survey_popup_text)).text
            if "Was braucht es" in survey_popup:
                print("Survey Popup Appeared")
                return True
        except TimeoutException:
            print("Survey popup did not appear")

    def click_survey_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.survey_button)).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == "https://docs.google.com/forms/d/e/1FAIpQLSd2W6MT67INXOIf2LFDXVNdZBHBKAkUKfQ5XJWkTyldLN1_Mw/viewform"
