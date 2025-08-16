from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class ResetPassword:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.heading = (By.XPATH, "//h3[contains(text(),'Set up new password')]")
        self.new_password = (By.CSS_SELECTOR, "input[name='newPassword']")
        self.repeat_new_password = (By.CSS_SELECTOR, "input[name='confirmPassword']")
        self.submit_button = (By.CSS_SELECTOR, "button[label='Submit']")

    def verify_heading(self):
        reset_password_screen_heading = self.wait.until(
            expected_conditions.visibility_of_element_located(self.heading)).text
        assert "Set up new password" in reset_password_screen_heading

    def set_new_password(self, password):
        self.driver.find_element(*self.new_password).send_keys(password)
        self.driver.find_element(*self.repeat_new_password).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def verify_reset_password_success(self):
        assert self.wait.until(expected_conditions.url_to_be("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/login"))
