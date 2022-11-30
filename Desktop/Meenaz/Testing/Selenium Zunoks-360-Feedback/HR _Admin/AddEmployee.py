from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime


EMAIL2 = "meenaz@apsis.com"
PASSWORD2 = "1234"

NAME = "abc"
EMAIL = "abc@apsis.com"
CONTACT = "1234567890"
REGION = "Pune"

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class addEmployee(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addEmployee(self):
        driver = self.driver
        try:
            driver.get("http://192.168.10.60:3000/sign-in")

        except Exception:
            file = open("Report.txt", "a")
            file.write(
                "\nAdd Employee: Fail\t Date:")
            file.write(dt_string)

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
            username.send_keys(EMAIL2)
            password.send_keys(PASSWORD2)
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
                    "\nAdd Employee: Fail\t Date:")
                file.write(dt_string)

            else:
                time.sleep(2)
                employee_tab = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/li[4]")
                employee_tab.click()
                time.sleep(2)
                employee = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/div[2]/button[2]")
                employee.click()
                time.sleep(2)
                name = driver.find_element(By.NAME, "name")
                email = driver.find_element(By.NAME, "email")
                contact = driver.find_element(By.NAME, "contact")
                region = driver.find_element(By.NAME, "region")
                department = driver.find_element(
                    By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div")
                designation = driver.find_element(
                    By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[2]/div/div/div/div")
                LM = driver.find_element(
                    By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[7]/div/div/div/div")
                SM = driver.find_element(
                    By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[8]/div/div/div/div")
                name.send_keys(NAME)
                email.send_keys(EMAIL)
                contact.send_keys(CONTACT)
                region.send_keys(REGION)
                time.sleep(2)
                action = ActionChains(driver)
                action.click(on_element=department).perform()
                time.sleep(1)
                action.send_keys(Keys.ARROW_DOWN).send_keys(
                    Keys.ENTER).perform()
                time.sleep(1)
                action.click(on_element=designation).perform()
                time.sleep(1)
                action.send_keys(Keys.ARROW_DOWN).send_keys(
                    Keys.ENTER).perform()
                time.sleep(1)
                action.click(on_element=LM).perform()
                time.sleep(1)
                action.send_keys(Keys.ARROW_DOWN).send_keys(
                    Keys.ENTER).perform()
                time.sleep(1)
                action.click(on_element=SM).perform()
                time.sleep(1)
                action.send_keys(Keys.ARROW_DOWN).send_keys(
                    Keys.ENTER).perform()
                time.sleep(2)
                save = driver.find_element(
                    By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[9]/div/button[2]")
                action.click(save).perform()
                time.sleep(5)
                try:
                    driver.find_element(
                        By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[1]/h2").click()
                    file = open("Manager_Report.txt", "a")
                    file.write(
                        "\nAdd Employee: Pass\t Date:")
                    file.write(dt_string)
                    file.close()
                except:
                    file = open("Manager_Report.txt", "a")
                    file.write(
                        "\nAdd Employee: Fail\t Date:")
                    file.write(dt_string)
                    file.close()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
