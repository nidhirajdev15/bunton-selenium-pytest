from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_basepage import BasePage
from pageObjects.pom_forgotpassword import ForgotPassword


class LoginPage(BasePage):
    email_field = (By.CSS_SELECTOR, "input[name='email']")
    password_field = (By.CSS_SELECTOR, "input[name='password']")
    submit_button = (By.CSS_SELECTOR, "button[type='submit']")
    forgot_password_button = (By.CSS_SELECTOR, "a[href='/forgot-password']")
    error_text = (By.CSS_SELECTOR, "p[id='my-helper-text']")
    dashboard_text = (By.XPATH, "//h1[normalize-space()='Ihr Dashboard']")

    def enter_login_email(self, email):
        self.perform_send_keys(self.email_field, email)

    def enter_login_password(self, password):
        self.perform_send_keys(self.password_field, password)

    def click_login_submit(self):
        self.wait_until_clickable_then_perform_click(self.submit_button)

    def validate_login_success(self):
        expected_url = "https://delightful-smoke-0bc51c803.5.azurestaticapps.net/dashboard"
        try:
            if self.wait.until(expected_conditions.url_to_be(expected_url)) and self.wait_until_visible(self.dashboard_text):
                print("Login successful: User redirected to the dashboard.")
                return True
        except Exception as e:
            try:
                error_message = self.wait_till_visible(self.error_text).text
                print(f"Login failed: Error message displayed - '{error_message}'")
                return False
            except Exception as e:
                print(f"An unexpected error occurred during login validation: {e}")
                return False
        return False

    def click_forgot_password(self):
        self.wait_until_clickable_then_perform_click(self.forgot_password_button)
        return ForgotPassword(self.driver, self.wait)
