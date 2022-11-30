from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver

        try:
            driver.get("https://accounts.google.com/")
            driver.maximize_window()
            time.sleep(2)
        except Exception:
            print(Exception)

        else:
            gmail = driver.find_element(By.CSS_SELECTOR, "#identifierId")
            gmail.send_keys("momin.meenaz29@gmail.com")
            time.sleep(2)
            driver.find_element(
                By.CSS_SELECTOR, ".VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.qIypjc.TrZEUc.lw1w4b").click()
            time.sleep(2)
            current_url = driver.current_url
            expected_url = "https://accounts.google.com/signin/v2/challenge"
            try:
                self.assertEqual(current_url, expected_url, "Failed!!!!!!!")
            except Exception:
                print(Exception)
            time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
