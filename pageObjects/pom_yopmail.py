from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_resetpassword import ResetPassword


class Yopmail:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.login_field = (By.CSS_SELECTOR, "input[id='login']")
        self.arrow_button = (By.CSS_SELECTOR, "div[id='refreshbut']")
        self.bunton_email = (By.XPATH, "//div[@class='lmfd']/span[contains(text(),'Bunton')]")
        self.bunton_email_text = (By.XPATH, "//div[@id='mail']//p[3]")
        # self.refresh_button = (By.CSS_SELECTOR, "button[id='refresh']")

    def fetch_verify_otp(self, email):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://yopmail.com/en/")
        username = email.split('@')[0]
        self.wait.until(
            expected_conditions.visibility_of_element_located(self.login_field)).send_keys(username)
        self.driver.find_element(*self.arrow_button).click()
        self.driver.switch_to.frame("ifinbox")
        self.wait.until(expected_conditions.visibility_of_element_located(self.bunton_email)).click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("ifmail")
        otp_text = self.wait.until(expected_conditions.visibility_of_element_located(self.bunton_email_text)).text  # "//p[contains(text(),'Your confirmation code')]"
        otp = otp_text.split(':')[-1].strip()
        self.driver.close() # This closes the current window (Yopmail)
        self.driver.switch_to.window(self.driver.window_handles[0])
        for i in range(5):
            self.wait.until(expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[aria-label*='Digit " + str(i + 1) + "']"))).send_keys(otp[i])
        return ResetPassword(self.driver, self.wait)
