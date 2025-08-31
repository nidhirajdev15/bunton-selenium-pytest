from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_basepage import BasePage


class ContactUs(BasePage):
    your_name = (By.CSS_SELECTOR, "input[name='name']")
    your_email = (By.CSS_SELECTOR, "input[name='email']")
    your_message = (By.CSS_SELECTOR, "div[class*='DraftStyleDefault']")
    send_button = (By.CSS_SELECTOR, "button[class*='css-1jze55c']")
    error_text = (By.CSS_SELECTOR, "p[id='my-helper-text']")

    def enter_your_name(self, name):
        self.perform_send_keys(self.your_name, name)

    def enter_your_email(self, email):
        self.perform_send_keys(self.your_email, email)

    def enter_message(self, message):
        self.perform_send_keys(self.your_message, message)

    def click_send(self):
        self.wait_until_visible_then_perform_click(self.send_button)

    def validate_send_message_success(self):
        error_elements = self.driver.find_elements(self.error_text)
        list_of_error_messages = [msg.text for msg in error_elements]
        assert not list_of_error_messages, f"Error message occurred as {list_of_error_messages}"
