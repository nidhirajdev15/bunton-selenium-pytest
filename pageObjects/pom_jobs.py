from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Jobs:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.search_field = (By.CSS_SELECTOR, "input[class*='css-dpd87z']")
        self.location_dropdown = (By.CSS_SELECTOR, "div[class*='css-n2qbr6'] div[class*='css-1i27l4i']")
        self.industry_dropdown = (By.CSS_SELECTOR, "div[class*='css-m43vlk'] > div:nth-child(1)")
        self.department_dropdown = (By.CSS_SELECTOR, "div[class*='css-m43vlk'] > div:nth-child(2)")
        self.experience_dropdown = (By.CSS_SELECTOR, "div[class*='css-m43vlk'] > div:nth-child(3)")
        self.dropdown_values = (By.CSS_SELECTOR, "ul[class*='css-jlcjk1'] li")
        self.job_types = (By.CSS_SELECTOR, "div[class*='css-1nzz3mm']")
        self.search_button = (By.CSS_SELECTOR, "button[class*='css-uja24m']")
        self.more_info_button = (By.CSS_SELECTOR, "a[class*='css-h8khix']")
        self.jobs_count = (By.CSS_SELECTOR, "div[class*='css-anxli']")

    def enter_search_keyword(self, search_keyword):
        self.wait.until(expected_conditions.visibility_of_element_located(self.search_field)).send_keys(search_keyword)

    def select_industry(self, industry):
        self.wait.until(expected_conditions.visibility_of_element_located(self.industry_dropdown)).click()
        industries = self.driver.find_elements(*self.dropdown_values)
        for ind in industries:
            if ind.text == industry:
                ind.click()
                break

    def select_department(self, department):
        self.wait.until(expected_conditions.visibility_of_element_located(self.department_dropdown)).click()
        departments = self.driver.find_elements(*self.dropdown_values)
        for dept in departments:
            if dept.text == department:
                dept.click()
                break

    def select_experience(self, experience):
        self.wait.until(expected_conditions.visibility_of_element_located(self.experience_dropdown)).click()
        experiences = self.driver.find_elements(*self.dropdown_values)
        for exp in experiences:
            if exp.text == experience:
                exp.click()
                break

    def select_location(self, location):
        self.wait.until(expected_conditions.visibility_of_element_located(self.location_dropdown)).click()
        locations = self.driver.find_elements(*self.dropdown_values)
        for loc in locations:
            if loc.text == location:
                loc.click()
                break

    def select_job_type(self, job_type):
        all_job_types = self.driver.find_elements(*self.job_types)
        for job in all_job_types:
            if job.text == job_type:
                job.click()
                break

    def click_search_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.search_button)).click()

    def click_more_info(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.more_info_button)).click()

    def validate_search_keyword_success(self):
        job_count_text = self.wait.until(expected_conditions.visibility_of_element_located(self.jobs_count)).text
        start_index = job_count_text.find('(')
        end_index = job_count_text.find(')')
