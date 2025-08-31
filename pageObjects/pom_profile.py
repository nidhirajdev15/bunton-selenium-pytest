from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_basepage import BasePage
from pageObjects.pom_myprofile import MyProfile


class Profile(BasePage):
    profile_icon = (By.CSS_SELECTOR, "div[class*='1241fla']")
    my_profile = (By.XPATH, "//h3[contains(text(),'My Profile')]")
    settings_button = (By.XPATH, "//h3[contains(text(),'Settings')]")
    logout_button = (By.XPATH, "//h3[contains(text(),'Logout')]")

    def click_profile_icon(self):
        self.wait_until_visible_then_perform_click(self.profile_icon)

    def click_my_profile(self):
        self.wait_until_visible_then_perform_click(self.my_profile)
        assert self.driver.current_url == "https://delightful-smoke-0bc51c803.5.azurestaticapps.net/my-profile"
        return MyProfile(self.driver, self.wait)

    def click_settings(self):
        self.wait_until_visible_then_perform_click(self.settings_button)

    def click_logout(self):
        self.wait_until_visible_then_perform_click(self.logout_button)
        assert self.driver.current_url == "https://delightful-smoke-0bc51c803.5.azurestaticapps.net/login"
