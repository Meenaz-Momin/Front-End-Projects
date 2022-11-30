from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

EMAIL = "channel.partner2@apsis.com"
PASSWORD = "1234"
COMPANY = "abc"
LOCATION = "pune"
ADMIN = "abc"
EMAIL2 = "abc@apsis.com"
EMPLOYEE_BASE = 10
ON_DATE = "20/11/2022"
END_DATE = "20/2/2023"
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class addTenant(unittest.TestCase):

    def test_addTenant(self):
        self.driver = webdriver.Chrome()
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
                                 "Test Case Failed")
            except:
                file = open("System_Admin_Report.txt", "a")
                file.write("\nLogin Test: Fail\t Date:")
                file.write(dt_string)
            else:
                tenant_tab = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/li[3]")
                tenant_tab.click()
                time.sleep(2)
                add = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a")
                add.click()
                time.sleep(2)

                company_name = driver.find_element(By.NAME, "name")
                location = driver.find_element(By.NAME, "location")
                email = driver.find_element(By.NAME, "email")
                admin = driver.find_element(By.NAME, "admin_name")
                employee_base = driver.find_element(By.NAME, "no_of_employee")
                industry = driver.find_element(
                    By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
                on_date = driver.find_element(By.NAME, "start_date")
                end_date = driver.find_element(By.NAME, "end_date")
                switch = driver.find_element(By.NAME, "is_active")

                action = ActionChains(driver)

                company_name.send_keys(COMPANY)
                location.send_keys(LOCATION)
                email.send_keys(EMAIL2)
                admin.send_keys(ADMIN)
                employee_base.send_keys(EMPLOYEE_BASE)
                on_date.send_keys(ON_DATE)
                end_date.send_keys(END_DATE)
                switch.click()
                action.click(industry).perform()
                time.sleep(1)
                action.send_keys(Keys.ARROW_DOWN).send_keys(
                    Keys.ENTER).perform()
                time.sleep(2)

                save = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
                save.click()
                time.sleep(2)

                cur_url = driver.current_url
                expected_url = "http://192.168.10.60:3000/admin/tenant-configration"
                try:
                    self.assertEqual(expected_url, cur_url, "url not matched")
                    file = open("System_Admin_Report.txt", "a")
                    file.write(
                        "\nAdd Tenant: Pass\t Date:")
                    file.write(dt_string)
                    file.close()

                except:
                    file = open("System_Admin_Report.txt", "a")
                    file.write(
                        "\nAdd Tenant: Fail\t Date:")
                    file.write(dt_string)
                    file.close()

            driver.quit()


if __name__ == "__main__":
    unittest.main()
