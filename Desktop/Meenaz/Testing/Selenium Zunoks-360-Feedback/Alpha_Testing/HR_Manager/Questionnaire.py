from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
Description = "Alpha Testing"


class QUESTIONNAIRE(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.10.60:3000/sign-in")
        self.driver.maximize_window()
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
        questionnaire_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/li[3]")))
        questionnaire_tab.click()
        time.sleep(2)
        create_questionnaire = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/li[3]")))
        create_questionnaire.click()
        time.sleep(2)

    def test_blankTitle(self):
        driver = self.driver
        time.sleep(2)
        title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.NAME, "title"
        )))
        description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.NAME, "description"
        )))
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div/div[5]/button")
        title.send_keys("")
        description.send_keys(Description)
        time.sleep(2)
        save.click()
        time.sleep(2)
        try:
            rows = len(driver.find_elements(
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div"))
            body.append(f"Blank Title: Fail    {dt_string}")
            assert False
        except:
            discard = driver.find_element(
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div/div[5]/a/button")
            discard.click()
            time.sleep()
            body.append(f"Blank Title: Pass    {dt_string}")
            assert True

    def test_blankDescription(self):
        driver = self.driver
        time.sleep(2)
        title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.NAME, "title"
        )))
        description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.NAME, "description"
        )))
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div/div[5]/button")
        title.send_keys(Title)
        description.send_keys("")
        time.sleep(2)
        save.click()
        time.sleep(2)
        try:
            rows = len(driver.find_elements(
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div"))
            body.append(f"Blank Description: Fail    {dt_string}")
            assert False
        except:
            discard = driver.find_element(
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div/div[5]/a/button")
            discard.click()
            time.sleep()
            body.append(f"Blank Description: Pass    {dt_string}")
            assert True

    def test_ZeroCompetency(self):
        driver = self.driver
        time.sleep(2)
        title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.NAME, "title"
        )))
        description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.NAME, "description"
        )))
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div/div[5]/button")
        title.send_keys(Title)
        description.send_keys(Description)
        time.sleep(2)
        save.click()
        time.sleep(2)
        save = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"")))
        save.click()
        time.sleep(3)
        try:
            rows = len(driver.find_elements(
                By.XPATH, ""))
            body.append(f"Zero Competency: Fail    {dt_string}")
            assert False
        except:
            Back = driver.find_element(
                By.XPATH, "")
            Back.click()
            time.sleep()
            body.append(f"Zero Competency: Pass    {dt_string}")
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
        #     subject = "HRMS-360 HR Manager:Add Questionnaire"
        #     # message = f"subject:{subject}\n\n{body[0]}\n{body[1]}\n{body[2]}\n{body[3]}\n{body[4]}\n{body[5]}\n{body[6]}\n{body[7]}\n"
        #     message = f"subject:{subject}\n\n{body}\n"
        #     smtp.sendmail(sender, receiver, message)
        #     print("Email Sent")
        self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(QUESTIONNAIRE("test_blankTitle"))
    suite.addTest(QUESTIONNAIRE("test_blankDescription"))
    suite.addTest(QUESTIONNAIRE("test_ZeroCompetency"))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
    # unittest.main()
