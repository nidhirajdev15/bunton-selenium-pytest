from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class ChangePassword:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.heading = (By.XPATH, "//h3[contains(text(),'Change Password')]")
        self.current_pwd = (By.CSS_SELECTOR, "input[name='currentPassword']")
        self.new_pwd = (By.CSS_SELECTOR, "input[name='newPassword']")
        self.repeat_new_pwd = (By.CSS_SELECTOR, "input[name='confirmPassword']")
        self.submit_button = (By.CSS_SELECTOR, "button[type='Submit']")
        self.notification_settings = (By.XPATH, "//button[contains(text(),'Notification Settings')]")
        self.error_text = (By.CSS_SELECTOR, "p[id='my-helper-text']")

    def verify_heading(self):
        change_pwd_heading = self.wait.until(expected_conditions.visibility_of_element_located(self.heading)).text
        assert "Change Password" in change_pwd_heading

    def set_current_password(self, current_password):
        self.driver.find_element(*self.current_pwd).send_keys(current_password)

    def set_new_password(self, new_password):
        self.driver.find_element(*self.new_pwd).send_keys(new_password)
        self.driver.find_element(*self.repeat_new_pwd).send_keys(new_password)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def validate_change_password_success(self):
        expected_url = "https://delightful-smoke-0bc51c803.5.azurestaticapps.net/dashboard"
        try:
            if self.wait.until(expected_conditions.url_to_be(expected_url)):
                print("Change password successful: User redirected to the dashboard.")
                return True
        except TimeoutException:
            try:
                error_message = self.wait.until(expected_conditions.visibility_of_element_located(self.error_text)).text
                print(f"Change password failed: Error message displayed - '{error_message}'")
                return False
            except Exception as e:
                print(f"An unexpected error occurred during change password validation: {e}")
                return False
