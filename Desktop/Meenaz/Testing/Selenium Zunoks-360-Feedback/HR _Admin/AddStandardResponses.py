from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from datetime import datetime

EMAIL = "meenaz@apsis.com"
PASSWORD = "1234"
LABEL = "Admin"
# LABEL = ""
SCORE = 4
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class addStandardResponses(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addStandardResponses(self):
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
                file = open("Manager_Report.txt", "a")
                file.write(
                    "\nAdd Standard Responses: Fail\t Date:")
                file.write(dt_string)

            else:
                time.sleep(2)
                setting_tab = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/div/li")
                setting_tab.click()
                time.sleep(1)
                standard_responses = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/div/div/div/div/div/li[1]")
                standard_responses.click()
                time.sleep(2)
                new = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button")
                new.click()
                time.sleep(1)
                label = driver.find_element(By.NAME, "label")
                score = driver.find_element(By.NAME, "score")
                save = driver.find_element(
                    By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div/button[2]")
                label.send_keys(LABEL)
                score.send_keys(SCORE)
                time.sleep(2)
                save.click()
                time.sleep(2)
                try:
                    driver.find_element(
                        By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]").click()
                    file = open("Manager_Report.txt", "a")
                    file.write(
                        "\nAdd Standard Responses: Pass\t Date:")
                    file.write(dt_string)
                except:
                    file = open("Manager_Report.txt", "a")
                    file.write(
                        "\nAdd Standard Responses: Fail\t Date:")
                    file.write(dt_string)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
