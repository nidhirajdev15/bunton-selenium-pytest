from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from utilities import excelReader


class RegistrationPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.excel_file_path = "C:\\Users\\nidhi.rajdev_infobea\\PycharmProjects\\SeleniumWithPython_Q1\\testData\\test_data.xlsx"
        self.start_button = (By.CSS_SELECTOR, "button[class*='css-11hb0im']")
        self.submit_button = (By.CSS_SELECTOR, "button[label='Submit']")
        self.fullname = (By.CSS_SELECTOR, "input[name='name']")
        self.experience = (By.XPATH, "//span[contains(text(),'"+excelReader.readData(self.excel_file_path, "RegistrationData", 2, 2)+"')]")
        self.business_network = (By.XPATH, "//span[contains(text(),'"+excelReader.readData(self.excel_file_path, "RegistrationData", 2, 3)+"')]")
        excel_departments = excelReader.readData(self.excel_file_path, "RegistrationData", 2, 4)
        excel_industries = excelReader.readData(self.excel_file_path, "RegistrationData", 2, 5)
        excel_locations = excelReader.readData(self.excel_file_path, "RegistrationData", 2, 6)
        self.departments = [item.strip() for item in excel_departments.split(',')]
        self.industries = [item.strip() for item in excel_industries.split(',')]
        self.locations = [item.strip() for item in excel_locations.split(',')]
        self.others_text_field = (By.CSS_SELECTOR, "input[placeholder='Others']")
        self.register_with_email_button = (By.CSS_SELECTOR, "button[class*='css-19bs668']")
        self.register_with_linkedin_button = (By.XPATH, "//span[contains(text(),'Register with Linkedin')]")
        self.register_with_google_button = (By.XPATH, "//span[contains(text(),'Register with Google')]")
        self.email_field = (By.CSS_SELECTOR, "input[name='email']")
        self.password_field = (By.CSS_SELECTOR, "input[name='password']")
        self.linkedin_email = (By.CSS_SELECTOR, "input[id='username']")
        self.linkedin_password = (By.CSS_SELECTOR, "input[id='password']")
        self.linkedin_sign_in = (By.CSS_SELECTOR, "button[type='submit']")
        self.accept_button = (By.CSS_SELECTOR, "input[type='checkbox']")
        self.error_text = (By.CSS_SELECTOR, "p[id='my-helper-text']")
        self.otp_heading = (By.XPATH, "//h5[contains(text(),'registration is complete')]")
        self.initial_window = self.driver.window_handles

    def answer_registration_questions(self, name):
        self.wait.until(expected_conditions.presence_of_element_located(self.start_button)).click()
        # log.info("clicking on Start button")
        self.wait.until(expected_conditions.presence_of_element_located(self.fullname)).send_keys(name)
        # log.info("Inputting user's full name")
        self.wait.until(expected_conditions.element_to_be_clickable(self.submit_button)).click()
        # log.info("clicking on Submit button")
        for item in self.departments:
            if "Others" in item:
                self.wait.until(expected_conditions.presence_of_element_located(
                    (By.XPATH, "//span[text()='Others']"))).click()
                start_index = item.find('(')
                end_index = item.find(')')
                self.wait.until(expected_conditions.visibility_of_element_located(self.others_text_field)).send_keys(item[start_index + 1:end_index])
            else:
                self.wait.until(expected_conditions.presence_of_element_located(
                    (By.XPATH, "//span[text()='"+item+"']"))).click()
        # log.info("choosing departments")
        self.wait.until(expected_conditions.element_to_be_clickable(self.submit_button)).click()
        # log.info("clicking on Submit button")
        self.wait.until(expected_conditions.presence_of_element_located(self.experience)).click()
        # log.info("choosing years of experience")
        self.wait.until(expected_conditions.element_to_be_clickable(self.submit_button)).click()
        # log.info("clicking on Submit button")
        for item in self.industries:
            if "Others" in item:
                self.wait.until(expected_conditions.presence_of_element_located(
                    (By.XPATH, "//span[text()='Others']"))).click()
                start_index = item.find('(')
                end_index = item.find(')')
                self.wait.until(expected_conditions.visibility_of_element_located(self.others_text_field)).send_keys(item[start_index + 1:end_index])
            else:
                self.wait.until(expected_conditions.presence_of_element_located(
                    (By.XPATH, "//span[text()='"+item+"']"))).click()
        # log.info("choosing Financial Services")
        self.wait.until(expected_conditions.element_to_be_clickable(self.submit_button)).click()
        # log.info("clicking on Submit button")
        for item in self.locations:
            if "Others" in item:
                self.wait.until(expected_conditions.presence_of_element_located(
                    (By.XPATH, "//span[text()='Others']"))).click()
                start_index = item.find('(')
                end_index = item.find(')')
                self.wait.until(expected_conditions.visibility_of_element_located(self.others_text_field)).send_keys(item[start_index + 1:end_index])
            else:
                self.wait.until(expected_conditions.presence_of_element_located(
                    (By.XPATH, "//span[text()='"+item+"']"))).click()
        # log.info("choosing the location")
        self.wait.until(expected_conditions.element_to_be_clickable(self.submit_button)).click()
        # log.info("clicking on Submit button")
        business_network = excelReader.readData(self.excel_file_path, "RegistrationData", 2, 3)
        if "Others" in business_network:
            self.wait.until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//span[text()='Others']"))).click()
            start_index = business_network.find('(')
            end_index = business_network.find(')')
            self.wait.until(expected_conditions.visibility_of_element_located(self.others_text_field)).send_keys(business_network[start_index + 1:end_index])
        else:
            self.wait.until(expected_conditions.element_to_be_clickable(self.business_network)).click()
        # log.info("choosing business network")
        self.wait.until(expected_conditions.element_to_be_clickable(self.submit_button)).click()
        # log.info("clicking on Submit button")

    def click_register_with_linkedin(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.register_with_linkedin_button)).click()
        # log.info("clicking on Register with LinkedIn button")

    def enter_linkedin_email_password(self, linkedin_email, linkedin_password):
        try:
            is_window_opened = self.wait.until(expected_conditions.new_window_is_opened(self.initial_window))
            if is_window_opened:
                print("Linkedin popup opened successfully")
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.wait.until(expected_conditions.visibility_of_element_located(self.linkedin_email)).send_keys(linkedin_email)
                self.wait.until(expected_conditions.visibility_of_element_located(self.linkedin_password)).send_keys(linkedin_password)
        except Exception as e:
            print("Linkedin popup did not open due to" + e)

    def click_linkedin_signin(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.linkedin_sign_in)).click()
        # self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_register_with_email(self):
        self.wait.until(
            expected_conditions.element_to_be_clickable(self.register_with_email_button)).click()
        # log.info("clicking on Register with Email button")

    def enter_email_password(self, email, password):
        self.wait.until(
            expected_conditions.presence_of_element_located(self.email_field)).send_keys(email)
        # log.info("entering email")
        self.driver.find_element(*self.password_field).send_keys(password)
        # log.info("entering password")

    def click_accept_terms(self):
        self.driver.find_element(*self.accept_button).click()
        # log.info("checking terms & conditions")

    def click_submit(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.submit_button)).click()
        # log.info("clicking on Submit button")

    def verify_registration_success(self):
        try:
            error_message = self.wait.until(expected_conditions.presence_of_element_located(self.error_text)).text
            error_occurred = True
            if error_occurred:
                print(f"Registration failed: Error message displayed - '{error_message}'")
                return False
        except Exception as e:
            try:
                otp_screen = self.wait.until(expected_conditions.presence_of_element_located(self.otp_heading)).text
                if otp_screen == "Your registration is complete.":
                    print("Registration successful. Next verify OTP")
                    return True
            except Exception as e:
                print(f"An unexpected error occurred during registration: {e}")
                return False
        return False
    # log.info("verify registration success")

    def verify_otp_success(self):
        otp_success = self.wait.until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h1[class*='css-1p5co88']"))).text
        assert "Welcome to bunton!" in otp_success
        print("Registration complete.")
        # log.info("verify OTP success")
