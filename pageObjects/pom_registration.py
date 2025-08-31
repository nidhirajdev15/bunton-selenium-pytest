from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pageObjects.pom_basepage import BasePage
from utilities import excelReader


class RegistrationPage(BasePage):
    excel_file_path = "C:\\Users\\nidhi.rajdev_infobea\\PycharmProjects\\SeleniumWithPython_Q1\\testData\\test_data.xlsx"
    start_button = (By.CSS_SELECTOR, "button[class*='css-11hb0im']")
    submit_button = (By.CSS_SELECTOR, "button[label='Submit']")
    fullname = (By.CSS_SELECTOR, "input[name='name']")
    experience = (By.XPATH, "//span[contains(text(),'"+excelReader.readData(excel_file_path, "RegistrationData", 2, 2)+"')]")
    business_network = (By.XPATH, "//span[contains(text(),'"+excelReader.readData(excel_file_path, "RegistrationData", 2, 3)+"')]")
    excel_departments = excelReader.readData(excel_file_path, "RegistrationData", 2, 4)
    excel_industries = excelReader.readData(excel_file_path, "RegistrationData", 2, 5)
    excel_locations = excelReader.readData(excel_file_path, "RegistrationData", 2, 6)
    departments = [item.strip() for item in excel_departments.split(',')]
    industries = [item.strip() for item in excel_industries.split(',')]
    locations = [item.strip() for item in excel_locations.split(',')]
    others_text_field = (By.CSS_SELECTOR, "input[placeholder='Others']")
    register_with_email_button = (By.CSS_SELECTOR, "button[class*='css-19bs668']")
    register_with_linkedin_button = (By.XPATH, "//span[contains(text(),'Register with Linkedin')]")
    register_with_google_button = (By.XPATH, "//span[contains(text(),'Register with Google')]")
    email_field = (By.CSS_SELECTOR, "input[name='email']")
    password_field = (By.CSS_SELECTOR, "input[name='password']")
    linkedin_email = (By.CSS_SELECTOR, "input[id='username']")
    linkedin_password = (By.CSS_SELECTOR, "input[id='password']")
    linkedin_sign_in = (By.CSS_SELECTOR, "button[type='submit']")
    accept_button = (By.CSS_SELECTOR, "input[type='checkbox']")
    error_text = (By.CSS_SELECTOR, "p[id='my-helper-text']")
    otp_heading = (By.XPATH, "//h5[contains(text(),'registration is complete')]")

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.initial_window = driver.window_handles

    def answer_registration_questions(self, name):
        self.wait_until_present_then_perform_click(self.start_button)
        # log.info("clicking on Start button")
        self.wait.until(expected_conditions.presence_of_element_located(self.fullname)).send_keys(name)
        # log.info("Inputting user's full name")
        self.wait_until_clickable_then_perform_click(self.submit_button)
        # log.info("clicking on Submit button")
        for item in self.departments:
            if "Others" in item:
                self.wait_until_present_then_perform_click((By.XPATH, "//span[text()='Others']"))
                start_index = item.find('(')
                end_index = item.find(')')
                self.perform_send_keys(self.others_text_field, item[start_index + 1:end_index])
            else:
                self.wait_until_present_then_perform_click((By.XPATH, "//span[text()='"+item+"']"))
        # log.info("choosing departments")
        self.wait_until_clickable_then_perform_click(self.submit_button)
        # log.info("clicking on Submit button")
        self.wait_until_present_then_perform_click(self.experience)
        # log.info("choosing years of experience")
        self.wait_until_clickable_then_perform_click(self.submit_button)
        # log.info("clicking on Submit button")
        for item in self.industries:
            if "Others" in item:
                self.wait_until_present_then_perform_click((By.XPATH, "//span[text()='Others']"))
                start_index = item.find('(')
                end_index = item.find(')')
                self.perform_send_keys(self.others_text_field, item[start_index + 1:end_index])
            else:
                self.wait_until_present_then_perform_click((By.XPATH, "//span[text()='"+item+"']"))
        # log.info("choosing Financial Services")
        self.wait_until_clickable_then_perform_click(self.submit_button)
        # log.info("clicking on Submit button")
        for item in self.locations:
            if "Others" in item:
                self.wait_until_present_then_perform_click((By.XPATH, "//span[text()='Others']"))
                start_index = item.find('(')
                end_index = item.find(')')
                self.perform_send_keys(self.others_text_field, item[start_index + 1:end_index])
            else:
                self.wait_until_present_then_perform_click((By.XPATH, "//span[text()='"+item+"']"))
        # log.info("choosing the location")
        self.wait_until_clickable_then_perform_click(self.submit_button)
        # log.info("clicking on Submit button")
        business_network = excelReader.readData(self.excel_file_path, "RegistrationData", 2, 3)
        if "Others" in business_network:
            self.wait_until_present_then_perform_click((By.XPATH, "//span[text()='Others']"))
            start_index = business_network.find('(')
            end_index = business_network.find(')')
            self.perform_send_keys(self.others_text_field, business_network[start_index + 1:end_index])
        else:
            self.wait_until_clickable_then_perform_click(self.business_network)
        # log.info("choosing business network")
        self.wait_until_clickable_then_perform_click(self.submit_button)
        # log.info("clicking on Submit button")

    def click_register_with_linkedin(self):
        self.wait_until_visible_then_perform_click(self.register_with_linkedin_button)
        # log.info("clicking on Register with LinkedIn button")

    def enter_linkedin_email_password(self, linkedin_email, linkedin_password):
        try:
            is_window_opened = self.wait.until(expected_conditions.new_window_is_opened(self.initial_window))
            if is_window_opened:
                print("Linkedin popup opened successfully")
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.perform_send_keys(self.linkedin_email, linkedin_email)
                self.perform_send_keys(self.linkedin_password, linkedin_password)
        except Exception as e:
            print("Linkedin popup did not open due to" + e)

    def click_linkedin_signin(self):
        self.wait_until_visible_then_perform_click(self.linkedin_sign_in)
        # self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_register_with_email(self):
        self.wait_until_clickable_then_perform_click(self.register_with_email_button)
        # log.info("clicking on Register with Email button")

    def enter_email_password(self, email, password):
        self.perform_send_keys(self.email_field, email)
        self.perform_send_keys(self.password_field, password)

    def click_accept_terms(self):
        self.wait_until_visible_then_perform_click(*self.accept_button)

    def click_submit(self):
        self.wait_until_clickable_then_perform_click(self.submit_button)

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
