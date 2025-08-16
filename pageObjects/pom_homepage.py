from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_buntonforcandidates import BuntonForCandidates
from pageObjects.pom_contactus import ContactUs
from pageObjects.pom_login import LoginPage
from pageObjects.pom_registration import RegistrationPage


class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.cookies_button = (By.CSS_SELECTOR, "button[label='Alle akzeptieren']")
        self.login_button = (By.CSS_SELECTOR, "div[class*='css-fke9tr'] > a:nth-of-type(2)")
        self.register_button = (By.CSS_SELECTOR, "div[class*='css-fke9tr'] > a:nth-of-type(1)")
        self.footer_contact_button = (By.CSS_SELECTOR, "//div[contains(@class,'css-isbt42')]/div[3]/div[1]/a")
        self.header_bunton_for_candidates = (By.CSS_SELECTOR, "a[class*='css-1s1rv8r']")
        self.header_bunton_for_companies = (By.XPATH, "//div[contains(@class,'css-pe2n1j')]/a[2]")
        self.header_jobs = (By.XPATH, "//div[contains(@class,'css-pe2n1j')]/a[3]")

    def accept_cookies(self):
        # accepting cookies
        self.wait.until(expected_conditions.element_to_be_clickable(self.cookies_button)).click()

    def click_login(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.login_button)).click()
        # log.info("clicking on Login button")
        return LoginPage(self.driver, self.wait)

    def click_register(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.register_button)).click()
        # log.info("clicking on Register button")
        return RegistrationPage(self.driver, self.wait)

    def click_contact_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.footer_contact_button)).click()
        return ContactUs(self.driver, self.wait)

    def click_header_bunton_for_candidates(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.header_bunton_for_candidates)).click()
        return BuntonForCandidates(self.driver, self.wait)

    def click_header_bunton_for_companies(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.header_bunton_for_companies)).click()

    def click_header_jobs(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.header_jobs)).click()
