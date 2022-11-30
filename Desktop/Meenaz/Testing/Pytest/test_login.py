from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time
import smtplib
from datetime import datetime
import pytest
import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

body = []
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
valid_mail = "meenaz@apsis.com"
invalid_mail = "meenaz123@apsis.com"
valid_password = "1234"
invalid_password = "12345"


class LOGIN(unittest.TestCase):
    
    @pytest.fixture(scope="session")
    def setUp():
        yield
        sender = "momin.meenaz29@gmail.com"
        receiver = "meenazm61@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = "HRMS-360 Automated Testing"
        body = "Body_of_the_mail"
        msg.attach(MIMEText(body, 'plain'))
        filename = "report.html"
        attachment = open(
            "/home/fladdra/Desktop/Meenaz/Pytest/report.html", "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender, "nxzjuoccxvzwrwec")
        text = msg.as_string()
        s.sendmail(sender, receiver, text)
        print("email sent")
        s.quit()

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.10.60:3000/sign-in")
        time.sleep(2)

    def test_invalidEmail(self):
        driver = self.driver
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "email")))
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "password")))
        visibility = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/div[1]/div/div[1]/div[2]/div/div/button")))
        signin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/div[1]/div/div[2]/button[1]")))
        time.sleep(2)
        email.send_keys(invalid_mail)
        password.send_keys(valid_password)
        time.sleep(1)
        visibility.click()
        time.sleep(2)
        signin.click()
        time.sleep(1)
        cur_url = driver.current_url
        expected_url = "http://192.168.10.60:3000/"
        try:
            self.assertNotEqual(cur_url, expected_url, "not equal")
            body.append(f"Test Invalid Email : Pass   {dt_string}")
            assert True
        except:
            body.append(f"Test Invalid Email : Fail    {dt_string}")
            assert False

    def test_invalidPassword(self):
        driver = self.driver
        time.sleep(2)
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "email")))
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "password")))
        signin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/div[1]/div/div[2]/button[1]")))
        email.send_keys(Keys.CONTROL + "a")
        email.send_keys(Keys.DELETE)
        password.send_keys(Keys.CONTROL + "a")
        password.send_keys(Keys.DELETE)
        time.sleep(2)
        email.send_keys(valid_mail)
        password.send_keys(invalid_password)
        time.sleep(2)
        signin.click()
        time.sleep(1)
        cur_url = driver.current_url
        expected_url = "http://192.168.10.60:3000/"
        try:
            self.assertNotEqual(cur_url, expected_url, "not equal")
            body.append(f"Test Invalid Password : Pass   {dt_string}")
            assert True
        except:
            body.append(f"Test Invalid Password : Fail    {dt_string}")
            assert False

    def test_blankField(self):
        driver = self.driver
        time.sleep(2)
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "email")))
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "password")))
        signin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/div[1]/div/div[2]/button[1]")))
        email.send_keys(Keys.CONTROL + "a")
        email.send_keys(Keys.DELETE)
        password.send_keys(Keys.CONTROL + "a")
        password.send_keys(Keys.DELETE)
        time.sleep(2)
        signin.click()
        time.sleep(1)
        cur_url = driver.current_url
        expected_url = "http://192.168.10.60:3000/"
        try:
            self.assertNotEqual(cur_url, expected_url, "not equal")
            body.append(f"Test Blank Field : Pass   {dt_string}")
            assert True
        except:
            body.append(f"Test Blank Field : Fail    {dt_string}")
            assert False

    def test_enterkey(self):
        driver = self.driver
        time.sleep(2)
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "email")))
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "password")))
        email.send_keys(Keys.CONTROL + "a")
        email.send_keys(Keys.DELETE)
        password.send_keys(Keys.CONTROL + "a")
        password.send_keys(Keys.DELETE)
        time.sleep(2)
        email.send_keys(valid_mail)
        password.send_keys(valid_password)
        time.sleep(2)
        Keys.ENTER
        time.sleep(1)
        cur_url = driver.current_url
        expected_url = "http://192.168.10.60:3000/"
        try:
            self.assertEqual(cur_url, expected_url, "not equal")
            body.append(f"Test Enter Key Working : Pass   {dt_string}")
            assert True
        except:
            body.append(f"Test Enter Key Working : Fail    {dt_string}")

    def test_validCredential(self):
        driver = self.driver
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "email")))
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "password")))
        signin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/div[1]/div/div[2]/button[1]")))
        email.send_keys(Keys.CONTROL + "a")
        email.send_keys(Keys.DELETE)
        password.send_keys(Keys.CONTROL + "a")
        password.send_keys(Keys.DELETE)
        time.sleep(2)
        email.send_keys(valid_mail)
        password.send_keys(valid_password)
        time.sleep(2)
        signin.click()
        time.sleep(2)
        cur_url = driver.current_url
        expected_url = "http://192.168.10.60:3000/"
        try:
            self.assertEqual(cur_url, expected_url, "not equal")
            body.append(f"Test Valid Credential : Pass   {dt_string}")
            assert True
        except:
            body.append(f"Test Valid Credential : Fail    {dt_string}")
            assert False

    @classmethod
    def tearDownClass(self):
        
        self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(LOGIN("test_invalidEmail"))
    suite.addTest(LOGIN("test_invalidPassword"))
    suite.addTest(LOGIN("test_blankField"))
    suite.addTest(LOGIN("test_enterkey"))
    suite.addTest(LOGIN("test_validCredential"))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
    # unittest.main()
