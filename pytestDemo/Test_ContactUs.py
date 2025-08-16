from selenium.webdriver.support import expected_conditions

from pageObjects.pom_contactus import ContactUs
from pageObjects.pom_homepage import HomePage


class Test_ContactUs:
    def test_contact_as_logged_out_user(self, invoke_browser_for_function):
        self.driver, self.wait = invoke_browser_for_function
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.contact = self.home.click_contact_button()
        assert self.wait.until(expected_conditions.url_contains("/contact-us"))
        self.contact.enter_your_name("Nidhi")
        self.contact.enter_your_email("nidhi.rajdev@infobeans.com")
        self.contact.enter_message("Test Message")
        self.contact.click_send()
        self.contact.validate_send_message_success()

    def test_contact_as_logged_in_user(self, login):
        self.driver, self.wait = login
        self.contact = ContactUs(self.driver, self.wait)
        self.contact.enter_message("Testing")
        self.contact.click_send()
        self.contact.validate_send_message_success()
