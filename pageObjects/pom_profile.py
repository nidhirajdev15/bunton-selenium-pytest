from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_myprofile import MyProfile


class Profile:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.profile_icon = (By.CSS_SELECTOR, "div[class*='1241fla']")
        self.my_profile = (By.XPATH, "//h3[contains(text(),'My Profile')]")
        self.settings_button = (By.XPATH, "//h3[contains(text(),'Settings')]")
        self.logout_button = (By.XPATH, "//h3[contains(text(),'Logout')]")

    def click_profile_icon(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.profile_icon)).click()

    def click_my_profile(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.my_profile)).click()
        assert self.driver.current_url == "https://delightful-smoke-0bc51c803.5.azurestaticapps.net/my-profile"
        return MyProfile(self.driver, self.wait)

    def click_settings(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.settings_button)).click()

    def click_logout(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.logout_button)).click()
        assert self.driver.current_url == "https://delightful-smoke-0bc51c803.5.azurestaticapps.net/login"
