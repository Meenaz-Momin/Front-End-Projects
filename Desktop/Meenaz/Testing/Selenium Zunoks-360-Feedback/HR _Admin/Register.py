from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

EMAIL = ""
PASSWORD = ""


class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_register(self):
        driver = self.driver

        try:
            driver.get("")
        except Exception:
            print(Exception)
        else:
            driver.maximize_window()
            time.sleep(2)
            email = driver.find_element(By.XPATH, "")
            password = driver.find_element(By.XPATH, "")
            register = driver.find_element(By.XPATH, "")
            email.send_keys(EMAIL)
            password.send_keys(PASSWORD)
            time.sleep(3)
            register.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
