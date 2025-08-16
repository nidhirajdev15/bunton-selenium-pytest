import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.pom_homepage import HomePage
from pageObjects.pom_login import LoginPage
from utilities import excelReader


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")


@pytest.fixture(scope="class")
# When you define a fixture with scope="class", the fixture is set up once before the first test method
# in a test class that uses the fixture.
# It is torn down after the last test method in that class has finished executing.
# Launches the browser once before the class, executes all tests, then closes the browser.
def invoke_browser_for_class(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-popup-blocking")
        # Launch chrome browser with options
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        # Launch firefox browser with options
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--disable-popup-blocking")
        driver = webdriver.Firefox(options=firefox_options)
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/")
    request.cls.driver = driver
    request.cls.wait = wait
    yield driver, wait
    driver.quit()


@pytest.fixture
# This means the fixture is set up once before each test function that uses it and torn down
# after that test function completes. Default scope is function
# Launches the browser before each test in a class
def invoke_browser_for_function(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-popup-blocking")
        # Launch chrome browser with options
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        # Launch firefox browser with options
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--disable-popup-blocking")
        driver = webdriver.Firefox(options=firefox_options)
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/")
    yield driver, wait
    driver.close()


@pytest.fixture()
def login(invoke_browser_for_function):
    driver, wait = invoke_browser_for_function
    home_page = HomePage(driver, wait)
    home_page.accept_cookies()
    home_page.click_login()
    assert wait.until(expected_conditions.url_contains("/login"))
    login_page = LoginPage(driver,wait)
    excel_file_path = "C:\\Users\\nidhi.rajdev_infobea\\PycharmProjects\\SeleniumWithPython_Q1\\testData\\test_data.xlsx"
    login_page.enter_login_email(excelReader.readData(excel_file_path, "LoginData", 2, 1))
    login_page.enter_login_password(excelReader.readData(excel_file_path, "LoginData", 2, 2))
    login_page.click_login_submit()
    assert login_page.validate_login_success() is True
    yield driver, wait
    pass
