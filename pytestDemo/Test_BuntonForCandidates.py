# import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_dashboard import Dashboard
from pageObjects.pom_homepage import HomePage


class Test_BuntonForCandidates:
    def test_buntonforcandidates_for_logged_out_user(self, invoke_browser_for_function):
        self.driver, self.wait = invoke_browser_for_function
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.bunton_for_candidates = self.home.click_header_bunton_for_candidates()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))
        original_window = self.driver.current_window_handle
        self.bunton_for_candidates.click_kostenlos_registrieren_or_ihr_dashboard_button()
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != original_window:
                self.driver.switch_to.window(window)
                assert self.wait.until(expected_conditions.url_contains("/registration"))
                assert self.wait.until(
                    expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "h5[class*='css-1utogp0']")))
                self.driver.close()
                break
        self.driver.switch_to.window(original_window)
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))
        self.bunton_for_candidates.hover_and_click_card1()
        self.bunton_for_candidates.validate_hover_and_click_success_logged_out()
        self.bunton_for_candidates.hover_and_click_card2()
        self.bunton_for_candidates.validate_hover_and_click_success_logged_out()
        self.bunton_for_candidates.hover_and_click_card3()
        self.bunton_for_candidates.validate_hover_and_click_success_logged_out()
        self.bunton_for_candidates.click_janet_recommendation()
        assert self.wait.until(expected_conditions.url_contains("/janet-recommendation"))
        assert self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[class*='css-1sghcfg']")))
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))
        self.bunton_for_candidates.click_about_bunton()
        assert self.wait.until(expected_conditions.url_contains("/about"))
        assert self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h6[text()='Why bunton?']")))
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))

    def test_buntonforcandidates_for_logged_in_user(self, login):
        self.driver, self.wait = login
        self.dashboard = Dashboard(self.driver, self.wait)
        self.bunton_for_candidate = self.dashboard.click_header_bunton_for_candidates()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))
        self.bunton_for_candidate.click_kostenlos_registrieren_or_ihr_dashboard_button()
        assert self.wait.until(expected_conditions.url_contains("/dashboard"))
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))
        self.bunton_for_candidate.hover_and_click_card1()
        self.bunton_for_candidate.validate_hover_and_click_success_logged_in()
        self.bunton_for_candidate.hover_and_click_card2()
        self.bunton_for_candidate.validate_hover_and_click_success_logged_in()
        self.bunton_for_candidate.hover_and_click_card3()
        self.bunton_for_candidate.validate_hover_and_click_success_logged_in()
        self.bunton_for_candidate.click_janet_recommendation()
        assert self.wait.until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[class*='css-1sghcfg']")))
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))
        self.bunton_for_candidate.click_about_bunton()
        assert self.wait.until(expected_conditions.url_contains("/about"))
        assert self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//h6[text()='Why bunton?']")))
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))