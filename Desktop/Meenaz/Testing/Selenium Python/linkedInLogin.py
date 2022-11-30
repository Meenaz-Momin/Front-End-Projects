from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import time


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        try:
            driver.get("https://in.linkedin.com/")
            driver.maximize_window()
        except Exception:
            print(Exception)
        else:
            time.sleep(2)
            driver.find_element(
                By.CSS_SELECTOR, ".nav__button-secondary.btn-md.btn-secondary-emphasis").click()
            current_url = driver.current_url
            expected_url = "https://www.linkedin.com/login"
            try:
                self.assertEqual(current_url, expected_url, "Failed!")
            except Exception:
                print(Exception)

            email = driver.find_element(By.CSS_SELECTOR, "#username")
            password = driver.find_element(By.CSS_SELECTOR, "#password")
            time.sleep(2)
            email.clear()
            password.clear()
            email.send_keys("momin.meenaz29@gmail.com")
            password.send_keys("meenaz123")

            driver.find_element(
                By.CSS_SELECTOR, "button[aria-label='Sign in']").click()
            time.sleep(3)

            current_url = driver.current_url
            expected_url = "https://www.linkedin.com/feed/"

            try:
                self.assertEqual(current_url, expected_url,
                                 "Not able to login")
            except Exception:
                print("incorrect credential")
            time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
