from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class ContactUs:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.your_name = (By.CSS_SELECTOR, "input[name='name']")
        self.your_email = (By.CSS_SELECTOR, "input[name='email']")
        self.your_message = (By.CSS_SELECTOR, "div[class*='DraftStyleDefault']")
        self.send_button = (By.CSS_SELECTOR, "button[class*='css-1jze55c']")
        self.error_text = (By.CSS_SELECTOR, "p[id='my-helper-text']")

    def enter_your_name(self, name):
        self.wait.until(expected_conditions.visibility_of_element_located(self.your_name)).send_keys(name)

    def enter_your_email(self, email):
        self.wait.until(expected_conditions.visibility_of_element_located(self.your_email)).send_keys(email)

    def enter_message(self, message):
        self.wait.until(expected_conditions.visibility_of_element_located(self.your_message)).send_keys(message)

    def click_send(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.send_button)).click()

    def validate_send_message_success(self):
        error_elements = self.driver.find_elements(self.error_text)
        list_of_error_messages = [msg.text for msg in error_elements]
        assert not list_of_error_messages, f"Error message occurred as {list_of_error_messages}"
