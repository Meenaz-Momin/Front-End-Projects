from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


EMAIL = "channel.partner@apsis.com"
PASSWORD = "1234"
# QUESTION =""
QUESTION = "Automated Testing"
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class addQuestions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addQuestions(self):
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
            time.sleep(5)

            cur_url = driver.current_url
            expected_url = "http://192.168.10.60:3000/admin/dashboard"

            try:
                self.assertEqual(expected_url, cur_url,
                                 "Result is not matched with expected")

            except Exception:
                file = open("System_Admin_Report.txt", "a")
                file.write(
                    "\nAdd Question: Fail\t Date:")
                file.write(dt_string)

            else:
                time.sleep(2)
                competency_tab = driver.find_element(
                    By.XPATH, "//*[@id = '__next']/div[1]/nav/div/div/div/ul/li[2]")
                competency_tab.click()
                time.sleep(1)
                cur_url = driver.current_url
                expected_url = "http://192.168.10.60:3000/competency-bank/standard"
                try:
                    self.assertEqual(expected_url, cur_url,
                                     "link doesn't match")
                except Exception:
                    file = open("System_Admin_Report.txt", "a")
                    file.write(
                        "\nAdd Question: Fail\t Date:")
                    file.write(dt_string)

                else:
                    time.sleep(2)
                    edit = driver.find_element(
                        By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/button[2]")
                    edit.click()
                    time.sleep(2)
                    questions = driver.find_element(
                        By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/div/button[2]")
                    questions.click()
                    time.sleep(2)
                    new = driver.find_element(
                        By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button")
                    new.click()
                    time.sleep(2)
                    question = driver.find_element(By.NAME, "text")
                    question.send_keys(QUESTION)
                    time.sleep(2)
                    action = ActionChains(driver)
                    area = driver.find_element(
                        By.XPATH, "//*[@id='main']/div[3]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
                    action.click(on_element=area).perform()
                    time.sleep(1)
                    action.send_keys(Keys.ARROW_DOWN).send_keys(
                        Keys.ENTER).perform()
                    time.sleep(1)
                    action.click(on_element=area).perform()
                    time.sleep(1)
                    action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(
                        Keys.ENTER).perform()
                    time.sleep(1)

                    type = driver.find_element(
                        By.XPATH, "//*[@id='main']/div[3]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
                    action.click(on_element=type).perform()
                    time.sleep(1)
                    action.send_keys(Keys.ARROW_DOWN).send_keys(
                        Keys.ENTER).perform()
                    time.sleep(2)
                    save = driver.find_element(
                        By.XPATH, "//button[@type='submit']")
                    save.click()
                    time.sleep(2)

                    try:
                        questions.click()
                        file = open("System_Admin_Report.txt", "a")
                        file.write(
                            "\nAdd Question: Pass\t Date:")
                        file.write(dt_string)

                    except:
                        file = open("System_Admin_Report.txt", "a")
                        file.write(
                            "\nAdd Question: Fail\t Date:")
                        file.write(dt_string)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
