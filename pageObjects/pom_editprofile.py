from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class EditProfile:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.your_name = (By.CSS_SELECTOR, "input[name='name']")
        self.your_profession = (By.CSS_SELECTOR, "input[name='profession']")
        self.view_resume = (By.CSS_SELECTOR, "a[class*='css-75lcn2']")
        self.about_you_text_box = (By.CSS_SELECTOR, "div[class*='DraftStyleDefault']")
        self.linkedin_url = (By.CSS_SELECTOR, "input[name='linkedinUrl']")
        self.business_network_yes = (By.XPATH, "//p[normalize-space()='Yes']")
        self.business_network_no = (By.XPATH, "//p[normalize-space()='No']")
        self.more_options = (By.CSS_SELECTOR, "button[id='more-options-button']")
        self.save_changes = (By.CSS_SELECTOR, "button[class*='css-oc9631']")
        self.delete_profile_button = (By.CSS_SELECTOR, "li[class*='css-nax6l8']")
        self.delete_profile_popup = (By.CSS_SELECTOR, "div[class*='css-a900in']")
        self.delete_popup_yes = (By.CSS_SELECTOR, "button[class*='css-1utx2x2']")
        self.delete_popup_no = (By.CSS_SELECTOR, "button[class*='css-einh80']")

    def click_more_options(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.more_options)).click()

    def click_delete_profile(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.delete_profile_button)).click()

    def click_yes_delete_profile(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.delete_popup_yes)).click()

    def click_no_delete_profile(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.delete_popup_no)).click()
        assert self.wait.until(expected_conditions.invisibility_of_element_located(self.delete_profile_popup)) is True

    def validate_delete_profile_success(self):
        assert self.wait.until(expected_conditions.url_to_be("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/login"))
