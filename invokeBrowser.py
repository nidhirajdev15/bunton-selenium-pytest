import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/nidhi.rajdev_infobea/Downloads/chromedriver-win64/chromedriver.exe")
chrome_options = webdriver.ChromeOptions
# chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(Service=service_obj, options=chrome_options)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")
time.sleep(2)
# Register a new user
driver.find_element(By.LINK_TEXT, "Create an Account").click()
driver.find_element(By.CSS_SELECTOR, "#firstname").send_keys("Test")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#lastname").send_keys("User")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='email_address']").send_keys("seleniumdemo@yopmail.com")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Automate123")
time.sleep(2)
driver.find_element(By.ID, "password-confirmation").send_keys("Automate123")
driver.implicitly_wait(3)
# driver.execute_script("window.scrollTo(0,1000)")
driver.find_element(By.XPATH, "//button[@class='action submit primary']").click()
driver.implicitly_wait(5)
registration_success = driver.find_element(By.XPATH, "//div[@class='page messages']").text
assert "Thank you for registering with Main Website Store." in registration_success
# driver.execute_script("arguments[0].click();", signup)
# print(driver.title)
# driver.find_element(By.CSS_SELECTOR,"input[id='user[first_name]']").send_keys("Test")
# driver.find_element(By.CSS_SELECTOR,"input[id='user[last_name]']").send_keys("User")
driver.quit()
