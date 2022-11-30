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
valid_mail = "meenaz.riyaz@apsissolutions.com"
valid_password = "ITSREUqF"
Title = "Alpha Testing"
Title255 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer jbmhh"
Title256 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer jbmhht"


class DESIGNATION(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.10.60:3000/sign-in")
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
        designation = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/div/div/div/div/div/li[4]")))
        designation.click()
        time.sleep(2)

    def test_blankTitle(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newDesignation = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button")))
            newDesignation.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div/button[2]")
            name.send_keys("")
            time.sleep(2)
            save.click()
            time.sleep(1)
            rows2 = len(driver.find_elements(
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))
            time.sleep(2)
            if(rows+1 == rows2):
                body.append(
                    f"Blank Field in Designation Name: Fail    {dt_string}")
                print(body)
                assert False
            else:
                cancel = driver.find_element(
                    By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]"
                )
                cancel.click()
                time.sleep(2)
                body.append(
                    f"Blank Field in Designation Name: Pass    {dt_string}")
                assert True

    def test_255Title(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newDesignation = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button")))
            newDesignation.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div/button[2]")
            name.send_keys(Title255)
            time.sleep(2)
            save.click()
            time.sleep(1)
            rows2 = len(driver.find_elements(
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))
            time.sleep(2)
            if(rows+1 == rows2):
                body.append(
                    f"255 Character in Designation Name: Pass    {dt_string}")
                assert True
            else:
                cancel = driver.find_element(
                    By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]"
                )
                cancel.click()
                time.sleep(2)
                body.append(
                    f"255 Character in Designation Name: Fail    {dt_string}")
                assert False

    def test_256Title(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newDesignation = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button")))
            newDesignation.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div/button[2]")
            name.send_keys(Title256)
            time.sleep(2)
            save.click()
            time.sleep(1)
            rows2 = len(driver.find_elements(
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))
            time.sleep(2)
            if(rows+1 == rows2):
                body.append(
                    f"256 Character in Designation Name: Fail    {dt_string}")
                assert False
            else:
                cancel = driver.find_element(
                    By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]"
                )
                cancel.click()
                time.sleep(2)
                body.append(
                    f"256 Character in Designation Name: Pass    {dt_string}")
                assert True

    def test_switchOff(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newDesignation = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button")))
            newDesignation.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            is_active = driver.find_element(By.NAME, "is_active")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div/button[2]")
            name.send_keys(Title)
            is_active.click()
            time.sleep(2)
            save.click()
            time.sleep(1)
            rows2 = len(driver.find_elements(
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))
            time.sleep(2)
            if(rows+1 == rows2):
                body.append(
                    f"is_Active Switch Off in Designation: Pass    {dt_string}")
                assert False
            else:
                try:
                    cancel = driver.find_element(
                        By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]"
                    )
                    cancel.click()
                    time.sleep(2)
                    body.append(
                        f"is_Active Switch Off in Designation: Fail    {dt_string}")
                    assert True
                except:
                    time.sleep(2)
                    body.append(
                        f"is_Active Switch Off in Designation: Fail    {dt_string}")
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
        #     subject = "HRMS-360 Alpha-Testing Login"
        #     message = f"subject:{subject}\n\n{body[0]}\n{body[1]}\n{body[2]}\n{body[3]}\n"
        #     smtp.sendmail(sender, receiver, message)
        #     print("Email Sent")
        self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DESIGNATION("test_blankTitle"))
    suite.addTest(DESIGNATION("test_255Title"))
    suite.addTest(DESIGNATION("test_256Title"))
    suite.addTest(DESIGNATION("test_switchOff"))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
    # unittest.main()
