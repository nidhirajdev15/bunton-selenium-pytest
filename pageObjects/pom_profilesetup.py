import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import random

from utilities import excelReader


class ProfileSetup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.excel_file_path = "C:\\Users\\nidhi.rajdev_infobea\\PycharmProjects\\SeleniumWithPython_Q1\\testData\\test_data.xlsx"
        self.education_sheet_name = "EducationData"
        self.experience_sheet_name = "WorkExperienceData"
        self.languages_sheet_name = "LanguagesData"
        self.additional_infos_sheet_name = "AdditionalInfoData"
        self.select_avatar_button = (By.CSS_SELECTOR, "button[label='Select an Avatar']")
        self.random_avatar = "//div[@class='MuiBox-root css-0']/ul/li["
        self.avatar_success_text = (By.XPATH, "//h2[contains(text(),'Thank you')]")
        self.education = (By.CSS_SELECTOR, "button[label='Education']")
        self.add_education = (By.CSS_SELECTOR, "button[label='Add education']")
        self.graduation_degree = (By.CSS_SELECTOR, "input[name='certificateDegreeName']")
        self.subject = (By.CSS_SELECTOR, "input[name='major']")
        self.year_of_completion_dropdown = (By.CSS_SELECTOR, "div[class*='css-1i27l4i']")
        self.year_of_completion_values = (By.CSS_SELECTOR, "li[class*='css-f885yq']")
        self.save_button = (By.CSS_SELECTOR, "button[label='Save']")
        self.work_experience = (By.CSS_SELECTOR, "button[label='Work Experience']")
        self.add_a_position = (By.CSS_SELECTOR, "button[label='Add a position']")
        self.job_title = (By.NAME, "jobTitle")
        self.company = (By.NAME, "companyName")
        self.department_dropdown = (By.XPATH, "//div[contains(text(), 'Select department')]")
        self.all_dropdown_values = (By.CSS_SELECTOR, "li[class*='css-ljk74r']")
        self.industry_dropdown = (By.XPATH, "//div[contains(text(), 'Select industry')]")
        self.start_month_dropdown = (By.CSS_SELECTOR, "div[class='MuiBox-root css-1rr4qq7'] div[class='MuiBox-root css-1rr4qq7'] div[class='MuiBox-root css-0']")
        self.start_year_dropdown = (By.CSS_SELECTOR, "div[class='MuiBox-root css-1rr4qq7'] div[class='MuiBox-root css-rzx6p5']")
        self.end_month_dropdown = (By.CSS_SELECTOR, "div[class='MuiBox-root css-1fvbz9o'] div[class='MuiBox-root css-1rr4qq7'] div[class='MuiBox-root css-0']")
        self.end_year_dropdown = (By.CSS_SELECTOR, "div[class='MuiBox-root css-1fvbz9o'] div[class='MuiBox-root css-rzx6p5']")
        self.currently_working_here = (By.CSS_SELECTOR, "span[class*='css-wvc5yg']")
        self.back_button = (By.CSS_SELECTOR, "div[class*='css-1so4p13'] span[class*='css-44vjup']")
        self.upload_resume = (By.CSS_SELECTOR, "button[label='Upload Resume']")
        self.languages = (By.CSS_SELECTOR, "button[label='Languages']")
        self.completion_percentage = (By.CSS_SELECTOR, "p[class*='css-19w6wr7']")
        self.error_text = (By.CSS_SELECTOR, "p[id='my-helper-text']")
        self.saved_education_experience_list = (By.CSS_SELECTOR, "div[class*='css-1u6liug']")
        self.saved_education_count = 0
        self.saved_work_experience_count = 0
        self.languages_button = (By.CSS_SELECTOR, "button[label='Languages']")
        self.languages_values = (By.CSS_SELECTOR, "ul[class*='css-hly6u8'] li")
        self.upload_resume = (By.CSS_SELECTOR, "button[label='Upload Resume']")
        self.resume_file = (By.CSS_SELECTOR, "div[class*='css-77qm15'] input[type='file']")
        self.upload_button = (By.CSS_SELECTOR, "p[class*='css-gels51']")
        self.additional_infos = (By.CSS_SELECTOR, "button[label='Additional Infos']")
        self.about_you_text_box = (By.CSS_SELECTOR, "div[class*='DraftEditor-content']")
        self.your_profession = (By.NAME, "profession")
        self.business_network_yes = (By.XPATH, "//div[@role='radiogroup']/label/p[contains(text(), 'Yes')]")
        self.business_network_no = (By.XPATH, "//div[@role='radiogroup']/label/p[contains(text(), 'No')]")
        self.business_network_others_field = (By.NAME, "otherProfessionalNetwork")
        self.preferences_others_field = (By.NAME, "otherBenefit")
        self.linkedin_profile_url = (By.NAME, "linkedinUrl")
        self.setup_later_button = (By.CSS_SELECTOR, "button[class*='css-c49n8t']")
        self.error_text = (By.CSS_SELECTOR, "p[id='my-helper-text']")

    def click_education(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.education)).click()
        try:
            assert self.wait.until(expected_conditions.url_contains("/addDetails/edu")) is True
        except Exception as e:
            print(f"Unable to navigate to add education screen due to: {e}")

    def add_save_education(self):
        user_graduation_degree_list = []
        user_subject_list = []
        user_year_of_completion_list = []
        number_of_rows = excelReader.getRowCount(self.excel_file_path, self.education_sheet_name)
        for education_data in range(3, number_of_rows + 1):
            user_graduation_degree_list.append(excelReader.readData(self.excel_file_path, self.education_sheet_name, education_data, 1))
            user_subject_list.append(excelReader.readData(self.excel_file_path, self.education_sheet_name, education_data, 2))
            user_year_of_completion_list.append(excelReader.readData(self.excel_file_path, self.education_sheet_name, education_data, 3))
        for item in range(0, number_of_rows - 2):
            self.wait.until(expected_conditions.visibility_of_element_located(self.add_education)).click()
            try:
                if self.wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//label[normalize-space()='Graduation degree*']"), "Graduation")):
                    self.driver.find_element(*self.graduation_degree).send_keys(user_graduation_degree_list[item])
                    self.driver.find_element(*self.subject).send_keys(user_subject_list[item])
                    self.driver.find_element(*self.year_of_completion_dropdown).click()
                    year_values = self.driver.find_elements(*self.year_of_completion_values)
                    for y in year_values:
                        if y.text == str(user_year_of_completion_list[item]):
                            y.click()
                            break
                    self.driver.find_element(*self.save_button).click()
                    try:
                        error_message = self.driver.find_element(*self.error_text).text
                        error_occurred = True
                        if error_occurred:
                            print(f"Unable to save the education details due to :{error_message}")
                    except Exception as e:
                        self.saved_education_count += 1
                        print(f"Education details saved successfully. No error message found.")
                        # else:
                        #     print(f"Year of completion is {user_year_of_completion}, hence skipping year: {y.text}")
            except Exception as e:
                print(f"Add education popup did not appear due to: {e}")

    def validate_education_save_success(self):
        saved_education_values = self.wait.until(expected_conditions.visibility_of_all_elements_located(self.saved_education_experience_list))
        assert self.saved_education_count == len(saved_education_values)
        time.sleep(5)
        self.wait.until(expected_conditions.presence_of_element_located(self.back_button)).click()
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, "button[label='Education'] span svg[data-testid='DoneIcon']")))
            print("Education details saved successfully")
        except Exception as e:
            print(f"Unable to save Education details due to :{e}")

    def click_work_experience(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.work_experience)).click()
        try:
            assert self.wait.until(expected_conditions.url_contains("/addDetails/exp")) is True
        except Exception as e:
            print(f"Unable to navigate to add experience screen due to :{e}")

    def add_save_work_experience(self):
        user_job_title = []
        user_company = []
        user_department = []
        user_industry = []
        user_start_month = []
        user_start_year = []
        user_currently_working_here = []
        user_end_month = []
        user_end_year = []
        number_of_rows = excelReader.getRowCount(self.excel_file_path, self.experience_sheet_name)
        for experience_data in range(3, number_of_rows + 1):
            user_job_title.append(excelReader.readData(self.excel_file_path, self.experience_sheet_name, experience_data, 1))
            user_company.append(excelReader.readData(self.excel_file_path, self.experience_sheet_name, experience_data, 2))
            user_department.append(excelReader.readData(self.excel_file_path, self.experience_sheet_name, experience_data, 3))
            user_industry.append(excelReader.readData(self.excel_file_path, self.experience_sheet_name, experience_data, 4))
            user_start_month.append(excelReader.readData(self.excel_file_path, self.experience_sheet_name, experience_data, 5))
            user_start_year.append(excelReader.readData(self.excel_file_path, self.experience_sheet_name, experience_data, 6))
            user_currently_working_here.append(excelReader.readData(self.excel_file_path, self.experience_sheet_name, experience_data, 7))
            user_end_month.append(excelReader.readData(self.excel_file_path, self.experience_sheet_name, experience_data, 8))
            user_end_year.append(excelReader.readData(self.excel_file_path, self.experience_sheet_name, experience_data, 9))
        for item in range(0, number_of_rows - 2):
            self.wait.until(expected_conditions.visibility_of_element_located(self.add_a_position)).click()
            try:
                if self.wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//label[normalize-space()='Job title*']"), "Job title")):
                    self.driver.find_element(*self.job_title).send_keys(user_job_title[item])
                    self.driver.find_element(*self.company).send_keys(user_company[item])
                    self.driver.find_element(*self.department_dropdown).click()
                    departments = self.driver.find_elements(*self.all_dropdown_values)
                    for dept in departments:
                        if dept.text == str(user_department[item]):
                            dept.click()
                            break
                    self.driver.find_element(*self.industry_dropdown).click()
                    industries = self.driver.find_elements(*self.all_dropdown_values)
                    for ind in industries:
                        if ind.text == str(user_industry[item]):
                            ind.click()
                            break
                    self.driver.find_element(*self.start_month_dropdown).click()
                    months = self.driver.find_elements(*self.all_dropdown_values)
                    for month in months:
                        if month.text == str(user_start_month[item]):
                            month.click()
                            break
                    self.driver.find_element(*self.start_year_dropdown).click()
                    years = self.driver.find_elements(*self.all_dropdown_values)
                    for year in years:
                        if year.text == str(user_start_year[item]):
                            year.click()
                            break
                    if user_currently_working_here[item] == "Yes":
                        self.driver.find_element(*self.currently_working_here).click()
                    else:
                        self.driver.find_element(*self.end_month_dropdown).click()
                        months = self.driver.find_elements(*self.all_dropdown_values)
                        for month in months:
                            if month.text == str(user_end_month[item]):
                                month.click()
                                break
                        self.driver.find_element(*self.end_year_dropdown).click()
                        years = self.driver.find_elements(*self.all_dropdown_values)
                        for year in years:
                            if year.text == str(user_end_year[item]):
                                year.click()
                                break
                    self.driver.find_element(*self.save_button).click()
                    try:
                        error_message = self.driver.find_element(*self.error_text).text
                        error_occurred = True
                        if error_occurred:
                            print(f"Unable to save the work experience details due to :{error_message}")
                    except Exception as e:
                        self.saved_work_experience_count += 1
                        print(f"Work Experience details saved successfully. No error message found due to {e}")
            except Exception as e:
                print(f"An error occurred due to: {e}")

    def validate_add_work_experience_success(self):
        saved_work_experience = self.wait.until(expected_conditions.visibility_of_all_elements_located(self.saved_education_experience_list))
        assert self.saved_work_experience_count == len(saved_work_experience)
        time.sleep(5)
        self.wait.until(expected_conditions.presence_of_element_located(self.back_button)).click()
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, "button[label='Work Experience'] span svg[data-testid='DoneIcon']")))
            print("Work Experience saved successfully")
        except Exception as e:
            print(f"Unable to save Work Experience due to :{e}")

    def click_languages(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.languages_button)).click()
            assert self.wait.until(expected_conditions.url_contains("/profileSetup/LanguagesDetail")) is True
        except Exception as e:
            print(f"Unable to navigate to Select Languages screen due to: {e}")

    def select_languages(self):
        languages_list = self.driver.find_elements(*self.languages_values)
        user_languages = excelReader.readData(self.excel_file_path, self.languages_sheet_name, 2, 1)
        user_languages_list = [language.strip() for language in user_languages.split(',')]
        for language in languages_list:
            if language.text in user_languages_list:
                language.click()

    def save_languages(self):
        try:
            self.driver.find_element(*self.save_button).click()
        except Exception as e:
            print(f"Unable to save the languages due to :{e}")

    def validate_select_languages_success(self):
        assert self.wait.until(expected_conditions.url_to_be("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/ProfileSetup")) is True
        try:
            self.driver.find_element(By.CSS_SELECTOR, "button[label='Languages'] span svg[data-testid='DoneIcon']")
            print("Languages saved successfully")
        except Exception as e:
            print(f"Languages not saved due to :{e}")

    def click_upload_resume(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.upload_resume)).click()

    def upload_resume_file(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.resume_file)).send_keys("C:\\Users\\nidhi.rajdev_infobea\\Downloads\\Mobile+QA.pdf")
        except Exception as e:
            print(f"I am in except block {e}")

    def click_upload_button(self):
        self.driver.find_element(*self.upload_button).click()
        try:
            error_message = self.driver.find_element(*self.error_text).text
            error_occurred = True
            if error_occurred and error_message:
                print(f"Unable to upload resume due to :{error_message}")
            else:
                print(f"Resume uploaded successfully.")
        except Exception as e:
            print(f"Resume uploaded successfully. No error message found due to {e}")

    def validate_resume_upload_success(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, "button[label='Upload Resume'] span svg[data-testid='DoneIcon']")))
            print("Resume uploaded successfully")
        except Exception as e:
            print(f"Resume upload failed due to :{e}")

    def click_select_avatar(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.select_avatar_button)).click()

    def select_avatar(self):
        random_number = random.randint(1, 20)
        avatar = self.random_avatar + str(random_number) + "]"
        time.sleep(5)
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, avatar))).click()

    def save_avatar(self):
        try:
            self.driver.find_element(*self.save_button).click()
        except Exception as e:
            print(f"Unable to save the languages due to :{e}")

    def validate_save_avatar_success(self):
        avatar_success = self.wait.until(expected_conditions.visibility_of_element_located(self.avatar_success_text)).text
        assert "Thank you for selecting your avatar." in avatar_success

    def click_additional_infos(self):
        time.sleep(4)
        self.wait.until(expected_conditions.visibility_of_element_located(self.additional_infos)).click()

    def enter_about_you(self):
        about_you_text = excelReader.readData(self.excel_file_path, "AdditionalInfoData", 3, 1)
        self.wait.until(expected_conditions.visibility_of_element_located(self.about_you_text_box)).send_keys(about_you_text)

    def enter_your_profession(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.your_profession)).send_keys(excelReader.readData(self.excel_file_path, "AdditionalInfoData", 3, 2))

    def select_business_network(self):
        is_business_member = excelReader.readData(self.excel_file_path, self.additional_infos_sheet_name, 3, 3)
        if is_business_member == "Yes":
            user_business_network = excelReader.readData(self.excel_file_path, self.additional_infos_sheet_name, 3, 4)
            user_business_network_list = [item.strip() for item in user_business_network.split(',')]
            for business_network in user_business_network_list:
                if "Others" in business_network:
                    self.driver.find_element(By.XPATH, "//p[contains(text(), '"+business_network+"')]").click()
                    start_index = business_network.find('(')
                    end_index = business_network.find(')')
                    self.driver.find_element(*self.business_network_others_field).send_keys(business_network[start_index+1: end_index])
                else:
                    self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(), '"+business_network+"')]"))).click()
        elif is_business_member == "No":
            self.driver.find_element(*self.business_network_no).click()

    def select_your_preferences(self):
        user_preferences = excelReader.readData(self.excel_file_path, self.additional_infos_sheet_name, 3, 5)
        user_preferences_list = [item.strip() for item in user_preferences.split(',')]
        for preferences in user_preferences_list:
            if "Others" in preferences:
                self.driver.find_element(By.XPATH, "//p[contains(text(), '"+preferences+"')]").click()
                start_index = preferences.find('(')
                end_index = preferences.find(')')
                self.driver.find_element(*self.preferences_others_field).send_keys(preferences[start_index+1:  end_index])
            else:
                self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(), '"+preferences+"')]"))).click()

    def enter_linkedin_url(self):
        linkedin_url = excelReader.readData(self.excel_file_path, self.additional_infos_sheet_name, 3, 6)
        self.wait.until(expected_conditions.visibility_of_element_located(self.linkedin_profile_url)).send_keys(linkedin_url)

    def click_save_additional_infos(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.save_button)).click()
        try:
            error_message = self.wait.until(expected_conditions.visibility_of_element_located(self.error_text)).text
            error_occurred = True
            if error_occurred:
                print(f"Unable to save additional info details due to :{error_message}")
        except Exception as E:
            try:
                assert self.wait.until(expected_conditions.url_to_be("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/ProfileSetup")) is True
            except Exception as e:
                print(f"Unable to save details due to: {e}")

    def validate_additional_info_save_success(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, "button[label='Additional Infos'] span svg[data-testid='DoneIcon']")))
            print("Additional info saved successfully")
        except Exception as e:
            print(f"Additional info save failed due to :{e}")
