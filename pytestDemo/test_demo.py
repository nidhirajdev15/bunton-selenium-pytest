# all files should start with name "test_" or end with "_test"
# all functions (test methods) should start with "test"
import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from pytestDemo.test_logging import Logging


# @pytest.mark.usefixtures("invoke_browser")
class TestRegistration:
    def test_registration(self, invoke_browser):
        driver, wait = invoke_browser
        # log = getLogger()
        driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1shxjz3']/a[2]").click()
        # log.info("clicking on Register button")
        time.sleep(3)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[class *='css-11hb0im']"))).click()
        # log.info("clicking on Start button")
        time.sleep(3)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[name='name']"))).send_keys("Nidhi")
        # log.info("Inputting user name")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "button[label='Submit']").click()
        # log.info("clicking on Submit button")
        time.sleep(3)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(),'Marketing')]"))).click()
        # log.info("clicking on Marketing")
        driver.find_element(By.XPATH, "//span[contains(text(),'Communication')]").click()
        # log.info("clicking on Communication")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "button[label='Submit']").click()
        # log.info("clicking on Submit button")
        time.sleep(3)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(),'0 - 5 years')]"))).click()
        # log.info("clicking on years of experience")
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[label='Submit']"))).click()
        time.sleep(3)
        # log.info("clicking on Submit button")
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(),'Financial Services')]"))).click()
        # log.info("clicking on Financial Services")
        driver.find_element(By.XPATH, "//span[contains(text(),'Testing')]").click()
        time.sleep(3)
        # log.info("clicking on Testing")
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[label='Submit']"))).click()
        time.sleep(3)
        # log.info("clicking on Submit button")
        driver.find_element(By.XPATH, "//span[contains(text(),'Berlin')]").click()
        time.sleep(3)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[label='Submit']"))).click()
        time.sleep(3)
        # log.info("clicking on Submit button")
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='css-19bs668']"))).click()
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']"))).send_keys("nidhirajdev10@yopmail.com")
        # log.info("entering email")
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Test@123")
        time.sleep(3)
        # log.info("entering password")
        driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
        # log.info("checking terms & conditions")
        time.sleep(3)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[label='Submit']"))).click()
        time.sleep(3)
        # log.info("clicking on Submit button")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://yopmail.com/en/")
        time.sleep(3)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[id='login']"))).send_keys("nidhirajdev10")
        driver.find_element(By.CSS_SELECTOR, "div[id='refreshbut']").click()
        time.sleep(3)
        driver.switch_to.frame("ifinbox")
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='lmfd']/span[contains(text(),'Bunton')]"))).click()
        driver.switch_to.default_content()
        driver.switch_to.frame("ifmail")
        otp_text = wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//p[contains(text(),'Your confirmation code')]"))).text  # "//div[@id='mail']//p[3]"
        otp = otp_text.split(':')[-1].strip()
        driver.switch_to.window(driver.window_handles[0])
        for i in range(5):
            wait.until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "input[aria-label*='Digit " + str(i + 1) + "']"))).send_keys(otp[i])
        time.sleep(3)
        reg_success = wait.until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h1[class*='css-1p5co88']"))).text
        assert "Welcome to bunton!" in reg_success
        # log.info("verify registration success")

    def test_login(self, invoke_browser):
        driver = invoke_browser
        driver.find_element(By.CSS_SELECTOR, "a[label='Login']").click()
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("nidhirajdev10@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Test@123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


# @pytest.mark.usefixtures("initiate")
# class TestExample:
#     def test_firstProgram(self):
#         print("Hello")
#
#     def test_secondProgram(self):
#         print("I will execute after initiate")
#
#
# @pytest.mark.usefixtures("data")
# class TestSecondExample(Logging):
#     def test_thirdProgram(self, data):
#         # print(data)
#         log = getLogger()
#         log.info(data)


# @pytest.mark.usefixtures("crossBrowser")
# def test_fourthProgram(crossBrowser):
#     print(crossBrowser)
