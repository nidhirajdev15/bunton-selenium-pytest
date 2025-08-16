import pytest
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_homepage import HomePage


@pytest.mark.usefixtures("invoke_browser_for_class")
class Test_HomePage:
    def test_bunton_for_candidates_logged_out_user(self):
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.home.click_header_bunton_for_candidates()
        assert self.wait.until(expected_conditions.url_contains("/candidate-homepage"))
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/"))

    def test_bunton_for_companies_logged_out_user(self):
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.home.click_header_bunton_for_companies()
        assert self.wait.until(expected_conditions.url_contains("/why-bunton"))
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/"))

    def test_jobs_logged_out_user(self):
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.home.click_header_jobs()
        assert self.wait.until(expected_conditions.url_contains("/job-list"))
        self.driver.back()
        assert self.wait.until(expected_conditions.url_contains("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/"))
