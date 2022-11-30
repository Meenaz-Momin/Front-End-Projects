from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from datetime import datetime
import re
# from Login import Test_Login

EMAIL = "meenaz@apsis.com"
PASSWORD = "1234"
TITLE = "comp1"
DESCRIPTION = "automated testing"
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class addCompetency(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addCompetency(self):
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
                    "\nAdd Competency: Fail\t Date:")
                file.write(dt_string)

            else:
                time.sleep(2)
                competency_tab = driver.find_element(
                    By.XPATH, "//*[@id = '__next']/div[1]/nav/div/div/div/ul/li[2]")
                competency_tab.click()
                time.sleep(1)
                cur_url = driver.current_url
                expected_url = "http://192.168.10.60:3000/competency-bank"
                try:
                    self.assertEqual(expected_url, cur_url,
                                     "link doesn't match")
                except Exception:
                    file = open("Manager_Report.txt", "a")
                    file.write(
                        "\nAdd Competency: Fail\t Date:")
                    file.write(dt_string)

                else:
                    add_competency = driver.find_element(
                        By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[3]")
                    add_competency.click()
                    time.sleep(2)
                    cur_url = driver.current_url
                    expected_url = "http://192.168.10.60:3000/competency-bank/add"

                    try:
                        self.assertEqual(
                            expected_url, cur_url, "Url not macthed")
                    except:
                        file = open("Manager_Report.txt", "a")
                        file.write(
                            "\nAdd Competency: Fail\t Date:")
                        file.write(dt_string)

                    else:
                        time.sleep(2)
                        title = driver.find_element(
                            By.NAME, "title")
                        description = driver.find_element(
                            By.NAME, "description")
                        save = driver.find_element(
                            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/form/div/div[5]/button[2]")
                        title.send_keys(TITLE)
                        description.send_keys(DESCRIPTION)
                        time.sleep(2)
                        save.click()
                        time.sleep(2)

                        cur_url = driver.current_url
                        expected_url = "http://192.168.10.60:3000/competency-bank/my/"

                        if(re.match(expected_url+'[a-zA-Z0-9]', cur_url)):
                            file = open("Manager_Report.txt", "a")
                            file.write(
                                "\nAdd Competency: Pass\t Date:")
                            file.write(dt_string)

                        else:
                            file = open("Manager_Report.txt", "a")
                            file.write(
                                "\nAdd Competency: Fail\t Date:")
                            file.write(dt_string)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
