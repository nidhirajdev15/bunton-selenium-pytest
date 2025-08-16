# To validate Login functionality
from selenium.webdriver.support import expected_conditions

from pageObjects.pom_homepage import HomePage
from utilities import excelReader


class Test_Login:

    excel_file_path = "C:\\Users\\nidhi.rajdev_infobea\\PycharmProjects\\SeleniumWithPython_Q1\\testData\\test_data.xlsx"
    number_of_rows = excelReader.getRowCount(excel_file_path, "LoginData")
    number_of_columns = excelReader.getColumnCount(excel_file_path, "LoginData")

    def test_login_with_valid_credentials(self, login):
        self.driver, self.wait = login

    def test_login_with_invalid_credentials(self, invoke_browser_for_function):
        self.driver, self.wait = invoke_browser_for_function
        self.home = HomePage(self.driver, self.wait)
        self.home.accept_cookies()
        self.loginPage = self.home.click_login()
        assert self.wait.until(expected_conditions.url_contains("/login"))
        self.loginPage.enter_login_email(excelReader.readData(self.excel_file_path, "LoginData", 3, 1))
        self.loginPage.enter_login_password(excelReader.readData(self.excel_file_path, "LoginData", 3, 2))
        self.loginPage.click_login_submit()
        assert self.loginPage.validate_login_success() is False
