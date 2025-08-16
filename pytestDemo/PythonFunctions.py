# import time
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions


from utilities import excelReader

excel_file_path = "C:\\Users\\nidhi.rajdev_infobea\\PycharmProjects\\SeleniumWithPython_Q1\\testData\\test_data.xlsx"
education_sheet_name = "EducationData"
user_graduation_degree_list = []
user_subject_list = []
user_year_of_completion_list = []
for degree in range(3, excelReader.getRowCount(excel_file_path, education_sheet_name) + 1):
    user_graduation_degree_list.append(excelReader.readData(excel_file_path, education_sheet_name, degree, 1))
    user_subject_list.append(excelReader.readData(excel_file_path, education_sheet_name, degree, 2))
    user_year_of_completion_list.append(excelReader.readData(excel_file_path, education_sheet_name, degree, 3))
print(user_graduation_degree_list)
print(user_subject_list)
print(user_year_of_completion_list)
#
# class Test_1:
#
#     def test_login(self, login):
#         self.driver, self.wait = login
#         self.excel_file_path = "C:\\Users\\nidhi.rajdev_infobea\\PycharmProjects\\SeleniumWithPython_Q1\\testData\\test_data.xlsx"
#         self.driver.get("https://delightful-smoke-0bc51c803.5.azurestaticapps.net/ProfileSetup")
#         self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[label='Upload Resume']"))).click()
#         time.sleep(3)
#         try:
#             self.wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[class*='css-77qm15'] input[type='file']"))).send_keys("C:\\Users\\nidhi.rajdev_infobea\\Downloads\\Mobile+QA.pdf")
#             print("I have executed send keys code")
#         except Exception as e:
#             print(f"I am in except block {e}")
#         time.sleep(3)
#         self.driver.find_element(By.CSS_SELECTOR, "p[class*='css-gels51']").click()
#         try:
#             time.sleep(3)
#             error_message = self.driver.find_element(By.CSS_SELECTOR, "p[id='my-helper-text']").text
#             time.sleep(3)
#             error_occurred = True
#             if error_occurred and error_message:
#                 print(f"Unable to upload resume due to :{error_message}")
#         except Exception as e:
#             print(f"Resume uploaded successfully. No error message found due to {e}")