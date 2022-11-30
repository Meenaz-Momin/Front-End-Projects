from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from datetime import datetime

EMAIL = "meenaz@apsis.com"
PASSWORD = "1234"
TITLE = "survey 1"
DESCRIPTION = "Automated Testing"
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class createSurvey(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_createSurvey(self):
        driver = self.driver
        try:
            driver.get("http://192.168.10.60:3000/sign-in")

        except Exception:
            print(Exception)
        else:
            driver.maximize_window()
            time.sleep(2)
            username = driver.find_element(
                By.NAME, "email")
            password = driver.find_element(
                By.NAME, "password")
            show_password = driver.find_element(By.CSS_SELECTOR, "svg")
            sign_in = driver.find_element(
                By.XPATH, "//button[normalize-space()='Sign in']")
            username.send_keys(EMAIL)
            password.send_keys(PASSWORD)
            time.sleep(2)
            show_password.click()
            time.sleep(2)
            sign_in.click()
            time.sleep(3)

            cur_url = driver.current_url
            expected_url = "http://192.168.10.60:3000/"

            try:
                self.assertEqual(expected_url, cur_url,
                                 "Result is not matched with expected")

            except Exception:
                print("something went wrong in matching urls")

            else:
                time.sleep(2)
                survey = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/li[6]")
                survey.click()
                time.sleep(2)
                new_Survey = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]")
                new_Survey.click()
                time.sleep(2)
                title = driver.find_element(By.NAME, "title")
                description = driver.find_element(By.NAME, "description")
                end_date = driver.find_element(By.NAME, "end_date")
                title.send_keys(TITLE)
                description.send_keys(DESCRIPTION)
                end_date.send_keys("17/11/2022")
                time.sleep(1)
                save = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/div[2]/div/div/div/div[7]/button[2]")
                save.click()
                time.sleep(2)
                employee_name = driver.find_element(
                    By.XPATH, "//*[@id='simple-tab-2']")
                employee_name.click()
                time.sleep(2)
                checkbox = driver.find_element(
                    By.XPATH, "//*[@id='simple-tabpanel-2']/div/div/div[1]/label/span[1]/input")
                checkbox.click()
                time.sleep(2)
                next = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/div[2]/div/div[4]/button[2]")
                next.click()
                time.sleep(2)
                radio = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/p/span/input")
                radio.click()
                time.sleep(2)
                next = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/button[2]")
                next.click()
                time.sleep(2)
                launch_survey = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/button[2]")
                launch_survey.click()
                time.sleep(2)

                cur_url = driver.current_url
                expected_url = "http://192.168.10.60:3000/survey/all"

                try:
                    self.assertEqual(expected_url, cur_url,
                                     "Test Case Failed")
                    file = open("Manager_Report.txt", "a")
                    file.write("\nCreate Survey: Pass\t Date:")
                    file.write(dt_string)

                except:
                    file = open("Manager_Report.txt", "a")
                    file.write("\nCreate Survey: Fail\t Date:")
                    file.write(dt_string)

                driver.quit()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
