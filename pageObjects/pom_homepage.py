from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_basepage import BasePage
from pageObjects.pom_buntonforcandidates import BuntonForCandidates
from pageObjects.pom_contactus import ContactUs
from pageObjects.pom_login import LoginPage
from pageObjects.pom_registration import RegistrationPage


class HomePage(BasePage):
    cookies_button = (By.CSS_SELECTOR, "button[label='Alle akzeptieren']")
    login_button = (By.CSS_SELECTOR, "div[class*='css-fke9tr'] > a:nth-of-type(2)")
    register_button = (By.CSS_SELECTOR, "div[class*='css-fke9tr'] > a:nth-of-type(1)")
    footer_contact_button = (By.CSS_SELECTOR, "//div[contains(@class,'css-isbt42')]/div[3]/div[1]/a")
    header_bunton_for_candidates = (By.CSS_SELECTOR, "a[class*='css-1s1rv8r']")
    header_bunton_for_companies = (By.XPATH, "//div[contains(@class,'css-pe2n1j')]/a[2]")
    header_jobs = (By.XPATH, "//div[contains(@class,'css-pe2n1j')]/a[3]")

    def accept_cookies(self):
        self.wait_until_visible_then_perform_click(self.cookies_button)

    def click_login(self):
        self.wait_until_clickable_then_perform_click(self.login_button)
        return LoginPage(self.driver, self.wait)

    def click_register(self):
        self.wait_until_visible_then_perform_click(self.register_button).click()
        return RegistrationPage(self.driver, self.wait)

    def click_contact_button(self):
        self.wait_until_visible_then_perform_click(self.footer_contact_button)
        return ContactUs(self.driver, self.wait)

    def click_header_bunton_for_candidates(self):
        self.wait_until_visible_then_perform_click(self.header_bunton_for_candidates)
        return BuntonForCandidates(self.driver, self.wait)

    def click_header_bunton_for_companies(self):
        self.wait_until_visible_then_perform_click(self.header_bunton_for_companies)

    def click_header_jobs(self):
        self.wait_until_visible_then_perform_click(self.header_jobs)
