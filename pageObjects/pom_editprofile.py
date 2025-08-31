from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_basepage import BasePage


class EditProfile(BasePage):
    your_name = (By.CSS_SELECTOR, "input[name='name']")
    your_profession = (By.CSS_SELECTOR, "input[name='profession']")
    view_resume = (By.CSS_SELECTOR, "a[class*='css-75lcn2']")
    about_you_text_box = (By.CSS_SELECTOR, "div[class*='DraftStyleDefault']")
    linkedin_url = (By.CSS_SELECTOR, "input[name='linkedinUrl']")
    business_network_yes = (By.XPATH, "//p[normalize-space()='Yes']")
    business_network_no = (By.XPATH, "//p[normalize-space()='No']")
    more_options = (By.CSS_SELECTOR, "button[id='more-options-button']")
    save_changes = (By.CSS_SELECTOR, "button[class*='css-oc9631']")
    delete_profile_button = (By.CSS_SELECTOR, "li[class*='css-nax6l8']")
    delete_profile_popup = (By.CSS_SELECTOR, "div[class*='css-a900in']")
    delete_popup_yes = (By.CSS_SELECTOR, "button[class*='css-1utx2x2']")
    delete_popup_no = (By.CSS_SELECTOR, "button[class*='css-einh80']")

    def click_more_options(self):
        self.wait_until_present_then_perform_click(self.more_options)

    def click_delete_profile(self):
        self.wait_until_present_then_perform_click(self.delete_profile_button)

    def click_yes_delete_profile(self):
        self.wait_until_visible_then_perform_click(self.delete_popup_yes)

    def click_no_delete_profile(self):
        self.wait_until_visible_then_perform_click(self.delete_popup_no)
        assert self.wait.until(expected_conditions.invisibility_of_element_located(self.delete_profile_popup)) is True

    def validate_delete_profile_success(self):
        assert self.wait.until(expected_conditions.url_to_be("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/login"))
