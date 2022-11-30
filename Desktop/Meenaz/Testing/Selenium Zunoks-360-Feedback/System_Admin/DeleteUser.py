from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from datetime import datetime


EMAIL = "channel.partner@apsis.com"
PASSWORD = "1234"
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class deleteUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_deleteUser(self):
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
            expected_url = "http://192.168.10.60:3000/admin/dashboard"

            try:
                self.assertEqual(expected_url, cur_url,
                                 "Result is not matched with expected")

            except Exception:
                file = open("System_Admin_Report.txt", "a")
                file.write(
                    "\nDelete User: Fail\t Date:")
                file.write(dt_string)

            else:
                time.sleep(2)
                setting_tab = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/div/li")
                setting_tab.click()
                time.sleep(1)
                user = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/div/div/div/div/div/li[1]")
                user.click()
                time.sleep(2)
                rows = len(driver.find_elements(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))
                delete = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/button[2]")
                delete.click()
                time.sleep(2)
                confirm = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div[2]/button[2]")
                confirm.click()
                # cancel = driver.find_element(
                #     By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div[2]/button[1]")
                # cancel.click()

                time.sleep(2)

                rows2 = len(driver.find_elements(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))

                if(rows2 < rows):
                    file = open("System_Admin_Report.txt", "a")
                    file.write(
                        "\nDelete User: Pass\t Date:")
                    file.write(dt_string)
                    file.close()

                else:
                    file = open("System_Admin_Report.txt", "a")
                    file.write(
                        "\nDelete User: Fail\t Date:")
                    file.write(dt_string)
                    file.close()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
