from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def wait_until_clickable(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))
    
    def wait_until_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))
    
    def wait_until_present(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))
    
    def wait_until_clickable_then_perform_click(self, locator):
        self.wait_until_clickable(locator).click()

    def wait_until_visible_then_perform_click(self, locator):
        self.wait_until_visible(locator).click()

    def wait_until_present_then_perform_click(self, locator):
        self.wait_until_present(locator).click()

    def perform_send_keys(self, locator, text):
        self.wait_until_visible(locator).send_keys(text)
