from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_yopmail import Yopmail


class ForgotPassword:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.enter_email = (By.CSS_SELECTOR, "input[name='email']")
        self.send_button = (By.CSS_SELECTOR, "button[label='Send']")
        self.error_text = (By.CSS_SELECTOR, "p[id='my-helper-text']")
        self.heading = (By.XPATH, "//h3[contains(text(),'Reset Password')]")

    def enter_forgotpwd_email(self, fp_email):
        self.driver.find_element(*self.enter_email).send_keys(fp_email)
        self.driver.find_element(*self.send_button).click()
        return Yopmail(self.driver, self.wait)

    def verify_email(self):
        try:
            error_message = self.wait.until(expected_conditions.visibility_of_element_located(self.error_text)).text
            print(f"Forgot Password failed: Error message displayed - '{error_message}'")
            return False
        except TimeoutException:
            try:
                heading = self.wait.until(expected_conditions.visibility_of_element_located(self.heading)).text
                if heading == "Reset Password":
                    print("Email verified. User can reset password.")
                    return True
            except Exception as e:
                print(f"An unexpected error occurred email validation: {e}")
                return False
        return False
