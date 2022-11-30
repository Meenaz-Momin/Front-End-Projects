from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time
import smtplib
from datetime import datetime

body = []
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
valid_mail = "safwan.shahid@apsissolutions.com"
valid_password = "W7Mi@mPz"
Name = "Shivani Rajput"
Email = "shivani.rajput@apsissolutions.com"
Region = "Pune"


class USERS(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(
            "http://192.168.1.171:3000/sign-in")
        driver = self.driver
        driver.maximize_window()
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "email")))
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "password")))
        signin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/div[1]/div/div[2]/button[1]")))
        time.sleep(2)
        email.send_keys(valid_mail)
        password.send_keys(valid_password)
        time.sleep(2)
        signin.click()
        time.sleep(2)
        setting = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/div/li")))
        setting.click()
        time.sleep(1)
        users = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/div/div/div/div/div/li[1]")))
        users.click()

    def test_blankName(self):
        driver = self.driver
        time.sleep(3)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newUser = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button")))
            newUser.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            email = driver.find_element(By.NAME, "email")
            region = driver.find_element(By.NAME, "region")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            name.send_keys("")
            email.send_keys(Email)
            region.send_keys(Region)
            time.sleep(2)
            save.click()
            time.sleep(1)
            rows2 = len(driver.find_elements(
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))
            time.sleep(2)
            if(rows+1 == rows2):
                body.append(
                    f"Blank Name Field in USERS: Fail    {dt_string}")
                print(body)
                assert False
            else:
                cancel = driver.find_element(
                    By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]"
                )
                cancel.click()
                time.sleep(2)
                body.append(
                    f"Blank Name Field in USERS: Pass    {dt_string}")
                assert True

    def test_blankEmail(self):
        driver = self.driver
        time.sleep(3)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newUser = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button")))
            newUser.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            email = driver.find_element(By.NAME, "email")
            region = driver.find_element(By.NAME, "region")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            name.send_keys(Name)
            email.send_keys("")
            region.send_keys(Region)
            time.sleep(2)
            save.click()
            time.sleep(1)
            rows2 = len(driver.find_elements(
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))
            time.sleep(2)
            if(rows+1 == rows2):
                body.append(
                    f"Blank Email Field in USERS: Fail    {dt_string}")
                print(body)
                assert False
            else:
                cancel = driver.find_element(
                    By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]"
                )
                cancel.click()
                time.sleep(2)
                body.append(
                    f"Blank Email Field in USERS: Pass    {dt_string}")
                assert True

    def test_blankRegion(self):
        driver = self.driver
        time.sleep(3)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newUser = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button")))
            newUser.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            email = driver.find_element(By.NAME, "email")
            region = driver.find_element(By.NAME, "region")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            name.send_keys(Name)
            email.send_keys(Email)
            region.send_keys("")
            time.sleep(2)
            save.click()
            time.sleep(1)
            rows2 = len(driver.find_elements(
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))
            time.sleep(2)
            if(rows+1 == rows2):
                body.append(
                    f"Blank Region Field in USERS: Fail    {dt_string}")
                print(body)
                assert False
            else:
                cancel = driver.find_element(
                    By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]"
                )
                cancel.click()
                time.sleep(2)
                body.append(
                    f"Blank Region Field in USERS: Pass    {dt_string}")
                assert True

    @classmethod
    def tearDownClass(self):
        # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        #     smtp.ehlo()
        #     smtp.starttls()
        #     smtp.ehlo()
        #     sender = "momin.meenaz29@gmail.com"
        #     password = "nxzjuoccxvzwrwec"
        #     receiver = "meenazm61@gmail.com"
        #     smtp.login(sender, password)
        #     subject = "HRMS-360 System Admin:Setting/Users"
        #     message = f"subject:{subject}\n\n{body[0]}\n{body[1]}\n{body[2]}\n"
        #     smtp.sendmail(sender, receiver, message)
        #     print("Email Sent")
        self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(USERS("test_blankName"))
    suite.addTest(USERS("test_blankEmail"))
    suite.addTest(USERS("test_blankRegion"))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
    # unittest.main()
