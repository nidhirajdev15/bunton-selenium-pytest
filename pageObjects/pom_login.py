from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_forgotpassword import ForgotPassword


class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.email = (By.CSS_SELECTOR, "input[name='email']")
        self.password = (By.CSS_SELECTOR, "input[name='password']")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.forgot_password_button = (By.CSS_SELECTOR, "a[href='/forgot-password']")
        self.error_text = (By.CSS_SELECTOR, "p[id='my-helper-text']")
        self.dashboard_text = (By.XPATH, "//h1[normalize-space()='Ihr Dashboard']")

    def enter_login_email(self, email):
        self.wait.until(expected_conditions.visibility_of_element_located(self.email)).send_keys(email)

    def enter_login_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def validate_login_success(self):
        expected_url = "https://delightful-smoke-0bc51c803.5.azurestaticapps.net/dashboard"
        try:
            if self.wait.until(expected_conditions.url_to_be(expected_url)) and self.wait.until(expected_conditions.visibility_of_element_located(self.dashboard_text)):
                print("Login successful: User redirected to the dashboard.")
                return True
        except Exception as e:
            try:
                error_message = self.wait.until(expected_conditions.visibility_of_element_located(self.error_text)).text
                print(f"Login failed: Error message displayed - '{error_message}'")
                return False
            except Exception as e:
                print(f"An unexpected error occurred during login validation: {e}")
                return False
        return False

    def click_forgot_password(self):
        self.driver.find_element(*self.forgot_password_button).click()
        return ForgotPassword(self.driver, self.wait)
