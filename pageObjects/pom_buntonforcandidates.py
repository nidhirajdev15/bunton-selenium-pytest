from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class BuntonForCandidates:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.kostenlos_registrieren_or_ihr_dashboard_button = (By.CSS_SELECTOR, "a[class*='css-jsix66']")
        self.card1 = (By.XPATH, "//div[contains(@class, 'css-1mgrifp')]/div[1]")
        self.card2 = (By.XPATH, "//div[contains(@class, 'css-1mgrifp')]/div[2]")
        self.card3 = (By.XPATH, "//div[contains(@class, 'css-1mgrifp')]/div[3]")
        self.button_on_cards = (By.CSS_SELECTOR, "a[class*='css-1d38pt9']")
        self.janet_recommendation = (By.CSS_SELECTOR, "div[class*='css-cm9gre']")
        self.about_bunton = (By.CSS_SELECTOR, "div[class*='css-kwc1p0']")
        self.registration_welcome_text = (By.CSS_SELECTOR, "h5[class*='css-1utogp0']")
        self.janet_image = (By.CSS_SELECTOR, "div[class*='css-1sghcfg']")
        self.about_bunton_text = (By.XPATH, "//h6[text()='Why bunton?']")

    def click_kostenlos_registrieren_or_ihr_dashboard_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.kostenlos_registrieren_or_ihr_dashboard_button)).click()

    def hover_and_click_card1(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.wait.until(expected_conditions.visibility_of_element_located(self.card1))).perform()
        self.wait.until(expected_conditions.presence_of_element_located(self.button_on_cards)).click()

    def hover_and_click_card2(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.wait.until(expected_conditions.visibility_of_element_located(self.card2))).perform()
        self.wait.until(expected_conditions.presence_of_element_located(self.button_on_cards)).click()

    def hover_and_click_card3(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.wait.until(expected_conditions.visibility_of_element_located(self.card3))).perform()
        self.wait.until(expected_conditions.presence_of_element_located(self.button_on_cards)).click()

    def validate_hover_and_click_success_logged_out(self):
        assert self.wait.until(expected_conditions.url_contains("/registration"))
        assert self.wait.until(expected_conditions.visibility_of_element_located(self.registration_welcome_text))
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))

    def validate_hover_and_click_success_logged_in(self):
        assert self.wait.until(expected_conditions.url_contains("/dashboard"))
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))

    def click_janet_recommendation(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.janet_recommendation)).click()

    def click_about_bunton(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.about_bunton)).click()
