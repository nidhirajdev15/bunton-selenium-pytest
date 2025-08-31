import random
import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.pom_buntonforcandidates import BuntonForCandidates

class Dashboard:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.header_bunton_for_candidates = (By.XPATH, "//div[contains(@class,'css-6n55t3')]/a[1]")
        self.header_bunton_for_companies = (By.XPATH, "//div[contains(@class,'css-6n55t3')]/a[2]")
        self.header_jobs = (By.XPATH, "//div[contains(@class,'css-6n55t3')]/a[3]")
        self.footer_imprint = (By.CSS_SELECTOR, "a[href='/imprint']")
        self.job_card_arrow_icon = (By.CSS_SELECTOR, "a[class*='css-1nitmmx']")

    def click_header_bunton_for_candidates(self):
        fluent_wait = WebDriverWait(self.driver, timeout=15, poll_frequency=0.5, ignored_exceptions=[ElementClickInterceptedException])
        element = fluent_wait.until(expected_conditions.element_to_be_clickable(self.header_bunton_for_candidates))
        time.sleep(5)
        element.click()
        return BuntonForCandidates(self.driver, self.wait)
    
    def click_header_bunton_for_companies(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.header_bunton_for_companies)).click()
        assert self.wait.until(expected_conditions.url_contains("/why-bunton"))

    def click_header_jobs(self):
        self.wait.until(expected_conditions. visibility_of_element_located(self.header_jobs)).click()
        assert self.wait.until(expected_conditions.url_contains("/job-list"))

    def click_random_job_card(self):
        all_job_cards = self.wait.until(expected_conditions.visibility_of_all_elements_located(self.job_card_arrow_icon))
        random_number = random.randint(1, len(all_job_cards))
        all_job_cards[random_number].click()
        assert self.wait.until(expected_conditions.url_contains("/job-details"))