from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_basepage import BasePage


class BuntonForCandidates(BasePage):
    kostenlos_registrieren_or_ihr_dashboard_button = (By.CSS_SELECTOR, "a[class*='css-jsix66']")
    card1 = (By.XPATH, "//div[contains(@class, 'css-1mgrifp')]/div[1]")
    card2 = (By.XPATH, "//div[contains(@class, 'css-1mgrifp')]/div[2]")
    card3 = (By.XPATH, "//div[contains(@class, 'css-1mgrifp')]/div[3]")
    button_on_cards = (By.CSS_SELECTOR, "a[class*='css-1d38pt9']")
    janet_recommendation = (By.CSS_SELECTOR, "div[class*='css-cm9gre']")
    about_bunton = (By.CSS_SELECTOR, "div[class*='css-kwc1p0']")
    registration_welcome_text = (By.CSS_SELECTOR, "h5[class*='css-1utogp0']")
    janet_image = (By.CSS_SELECTOR, "div[class*='css-1sghcfg']")
    about_bunton_text = (By.XPATH, "//h6[text()='Why bunton?']")

    def click_kostenlos_registrieren_or_ihr_dashboard_button(self):
        self.wait_until_visible_then_perform_click(self.kostenlos_registrieren_or_ihr_dashboard_button)

    def hover_and_click_card1(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.wait_until_visible(self.card1)).perform()
        self.wait_until_present_then_perform_click(self.button_on_cards)

    def hover_and_click_card2(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.wait_until_visible(self.card2)).perform()
        self.wait_until_present_then_perform_click(self.button_on_cards)

    def hover_and_click_card3(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.wait_until_visible(self.card3)).perform()
        self.wait_until_present_then_perform_click(self.button_on_cards)

    def validate_hover_and_click_success_logged_out(self):
        assert self.wait.until(expected_conditions.url_contains("/registration"))
        assert self.wait_until_visible(self.registration_welcome_text)
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))

    def validate_hover_and_click_success_logged_in(self):
        assert self.wait.until(expected_conditions.url_contains("/dashboard"))
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))

    def click_janet_recommendation(self):
        self.wait_until_visible_then_perform_click(self.janet_recommendation)

    def click_about_bunton(self):
        self.wait_until_visible_then_perform_click(self.about_bunton)
