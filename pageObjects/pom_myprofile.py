import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_editprofile import EditProfile
from pageObjects.pom_profilesetup import ProfileSetup


class MyProfile(ProfileSetup):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait
        self.edit_pencil_icon = (By.CSS_SELECTOR, "a[href='/edit-profile/']")
        self.edit_avatar_button = (By.CSS_SELECTOR, "button[class*='css-lzoaj5']")
        self.download_resume_button = (By.CSS_SELECTOR, "a[class*='css-436sm']")
        self.experience_button = (By.CSS_SELECTOR, "button[class*='css-1cvxo17'] h3[class*='css-l615y6']")
        self.education_button = (By.CSS_SELECTOR, "button[class*='css-ij1f6l'] h3[class*='css-l615y6']")
        self.add_plus_icon = (By.CSS_SELECTOR, "div[class*='css-11j9yrv']")
        self.edit_education_experience_icon = (By.CSS_SELECTOR, "div[class*='css-frn5g']")
        self.delete_education_experience_icon = (By.CSS_SELECTOR, "div[class*='css-1rsdp6v']")
        self.delete_popup_yes = (By.CSS_SELECTOR, "button[class*='css-1utx2x2']")
        self.delete_popup_no = (By.CSS_SELECTOR, "button[class*='css-einh80']")

    def download_resume(self):
        original_window = self.driver.window_handles
        self.wait.until(expected_conditions.visibility_of_element_located(self.download_resume_button)).click()
        is_new_window_opened = self.wait.until(expected_conditions.new_window_is_opened(original_window))
        try:
            assert is_new_window_opened is True
        except Exception as e:
            print(f"Download Resume did not open new window, error occurred as: {e}")

    def profile_edit_avatar(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.edit_avatar_button)).click()
        super().select_avatar()

    def profile_save_avatar(self):
        super().save_avatar()
        super().validate_save_avatar_success()

    def profile_click_education(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.education_button)).click()

    def profile_add_education(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.add_plus_icon)).click()
        super().add_save_education()

    def profile_click_experience(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.experience_button)).click()

    def profile_add_experience(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.add_plus_icon)).click()
        super().add_save_work_experience()

    def profile_delete_education_or_experience(self):
        all_records = self.driver.find_elements(*self.delete_education_experience_icon)
        number_of_records = len(all_records)
        random_number = random.randint(0, number_of_records)
        all_records[random_number].click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.delete_popup_yes)).click()
        updated_records = self.driver.find_elements(*self.delete_education_experience_icon)
        number_of_records_after_deletion = len(updated_records)
        assert number_of_records_after_deletion == number_of_records - 1

    def profile_click_edit_pencil_icon(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.edit_pencil_icon)).click()
        assert self.driver.current_url == "https://delightful-smoke-0bc51c803.5.azurestaticapps.net/edit-profile/"
        return EditProfile(self.driver, self.wait)
