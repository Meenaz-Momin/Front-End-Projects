from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from datetime import datetime


EMAIL = "meenaz@apsis.com"
PASSWORD = "1234"
CATEGORY = "Updated text"
NO_OF_RATERS = 5
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class editRaters(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_editRaters(self):
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
                    "\nEdit Designation: Fail\t Date:")
                file.write(dt_string)
            else:
                time.sleep(2)
                setting_tab = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/div/li")
                setting_tab.click()
                time.sleep(1)
                raters = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/div/div/div/div/div/li[5]")
                raters.click()
                time.sleep(2)
                rows = len(driver.find_elements(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))
                edit = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[5]/div/button[1]")
                edit.click()
                time.sleep(2)
                category = driver.find_element(By.NAME, "category_name")
                no_of_raters = driver.find_element(By.NAME, "no_of_raters")
                is_required = driver.find_element(By.NAME, "is_required")
                is_external = driver.find_element(By.NAME, "is_external")
                category.clear()
                category.send_keys(CATEGORY)
                no_of_raters.send_keys(NO_OF_RATERS)
                is_required.click()
                is_external.click()
                is_required.click()
                time.sleep(2)
                save = driver.find_element(
                    By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[5]/div/button[2]")
                save.click()
                time.sleep(2)

                rows2 = len(driver.find_elements(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))

                if(rows2 == rows):
                    file = open("Manager_Report.txt", "a")
                    file.write(
                        "\nEdit Raters Category: Pass\t Date:")
                    file.write(dt_string)
                    file.close()

                else:
                    file = open("Manager_Report.txt", "a")
                    file.write(
                        "\nEdit Raters Category: Fail\t Date:")
                    file.write(dt_string)
                    file.close()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
