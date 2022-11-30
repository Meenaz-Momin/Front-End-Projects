from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from datetime import datetime
import smtplib

EMAIL = "meenaz@apsis.com"
PASSWORD = "1234"
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class Test_Login(unittest.TestCase):

    def test_login(self):
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
            expected_url = "http://192.168.10.60:3000/"

            try:
                self.assertEqual(expected_url, cur_url,
                                 "Test Case Failed")
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    sender = "momin.meenaz29@gmail.com"
                    password = "nxzjuoccxvzwrwec"
                    receiver = "meenazm61@gmail.com"
                    smtp.login(sender, password)
                    subject = "HRMS-360 Automated Testing"
                    body = "Login Test: Pass\t\t", dt_string
                    message = f'subject:{subject}\n\n{body}'
                    smtp.sendmail(sender, receiver, message)
                    print("email sent")

            except:
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()
                    sender = "momin.meenaz29@gmail.com"
                    password = "nxzjuoccxvzwrwec"
                    receiver = "meenazm61@gmail.com"
                    smtp.login(sender, password)
                    subject = "HRMS-360 Automated Testing"
                    body = "Login Test: Fail\t\t", dt_string
                    message = f'subject:{subject}\n\n{body}'
                    smtp.sendmail(sender, receiver, message)
                    print("email sent")

            driver.quit()


if __name__ == "__main__":
    unittest.main()
