from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time
import smtplib
from datetime import datetime
import re

body = []
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
valid_mail = "meenaz.riyaz@apsissolutions.com"
valid_password = "ITSREUqF"
Title = "Alpha Testing"
Description = "Alpha Testing"
Titlemorethan255 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer eget abhy"
Descriptionmorethan255 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer eget abhy"
Title255 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer egetv"
Description255 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer egetv"


class COMPETENCY_ADMIN(unittest.TestCase):

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
        competency_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/li[2]")))
        competency_tab.click()
        time.sleep(2)

    def test_BothBlankField(self):
        driver = self.driver
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            newCompetency = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button")))
            newCompetency.click()
            time.sleep(2)
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "title")))
            description = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "description")))
            save = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/form/div/div[5]/button[2]")))
            title.send_keys("")
            description.send_keys("")
            time.sleep(2)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Leave Competency Title and Description Blank: Fail    {dt_string}")
                assert False
            else:
                body.append(
                    f"Leave Competency Title and Description Blank: Pass    {dt_string}")
                assert True

    def test_BlankTitle(self):
        driver = self.driver
        try:
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "title")))
        except:
            driver.get("http://192.168.1.171:3000/competency-bank/add")
        description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "description")))
        save = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/form/div/div[5]/button[2]")))
        title.send_keys("")
        description.send_keys(Description)
        time.sleep(2)
        save.click()
        time.sleep(2)
        cur_url = driver.current_url
        expected_url = "http://192.168.10.60:3000/competency-bank/my"
        if(re.match(expected_url+'[a-zA-Z0-9]', cur_url)):
            body.append(
                f"Leave Competency Title Blank: Fail    {dt_string}")
            assert False
        else:
            body.append(
                f"Leave Competency Title Blank: Pass    {dt_string}")
            assert True

    def test_BlankDescription(self):
        driver = self.driver
        try:
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "title")))
        except:
            driver.get("http://192.168.1.171:3000/competency-bank/add")
        description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "description")))
        save = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/form/div/div[5]/button[2]")))
        title.send_keys(Keys.CONTROL + "a")
        title.send_keys(Keys.DELETE)
        description.send_keys(Keys.CONTROL + "a")
        description.send_keys(Keys.DELETE)
        time.sleep(2)
        title.send_keys(Title)
        description.send_keys("")
        time.sleep(2)
        save.click()
        time.sleep(2)
        cur_url = driver.current_url
        expected_url = "http://192.168.10.60:3000/competency-bank/my"
        if(re.match(expected_url+'[a-zA-Z0-9]', cur_url)):
            body.append(
                f"Leave Competency Description Blank: Fail    {dt_string}")
            assert False
        else:
            body.append(
                f"Leave Competency Description Blank: Pass    {dt_string}")
            assert True

    def test_title256(self):
        driver = self.driver
        try:
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "title")))
        except:
            driver.get("http://192.168.1.171:3000/competency-bank/add")
        description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "description")))
        save = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/form/div/div[5]/button[2]")))
        title.send_keys(Keys.CONTROL + "a")
        title.send_keys(Keys.DELETE)
        description.send_keys(Keys.CONTROL + "a")
        description.send_keys(Keys.DELETE)
        time.sleep(2)
        title.send_keys(Titlemorethan255)
        description.send_keys(Description)
        time.sleep(2)
        save.click()
        time.sleep(2)
        cur_url = driver.current_url
        expected_url = "http://192.168.10.60:3000/competency-bank/my"
        if(re.match(expected_url+'[a-zA-Z0-9]', cur_url)):
            body.append(
                f"Competency Title More Than 255 Characters: Fail    {dt_string}")
            assert False
        else:
            body.append(
                f"Competency Title More Than 255 Characters: Pass    {dt_string}")
            assert True

    def test_description256(self):
        driver = self.driver
        try:
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "title")))
        except:
            driver.get("http://192.168.1.171:3000/competency-bank/add")
        description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "description")))
        save = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/form/div/div[5]/button[2]")))
        title.send_keys(Keys.CONTROL + "a")
        title.send_keys(Keys.DELETE)
        description.send_keys(Keys.CONTROL + "a")
        description.send_keys(Keys.DELETE)
        time.sleep(2)
        title.send_keys(Title)
        description.send_keys(Descriptionmorethan255)
        time.sleep(2)
        save.click()
        time.sleep(2)
        cur_url = driver.current_url
        expected_url = "http://192.168.10.60:3000/competency-bank/my"
        if(re.match(expected_url+'[a-zA-Z0-9]', cur_url)):
            body.append(
                f"Competency Description More Than 255 Characters: Fail    {dt_string}")
            assert False
        else:
            body.append(
                f"Competency Description More Than 255 Characters: Pass    {dt_string}")
            assert True

    def test_title255(self):
        driver = self.driver
        try:
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "title")))
        except:
            driver.get("http://192.168.1.171:3000/competency-bank/add")
        description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "description")))
        save = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/form/div/div[5]/button[2]")))
        title.send_keys(Keys.CONTROL + "a")
        title.send_keys(Keys.DELETE)
        description.send_keys(Keys.CONTROL + "a")
        description.send_keys(Keys.DELETE)
        time.sleep(2)
        title.send_keys(Title255)
        description.send_keys(Description)
        time.sleep(2)
        save.click()
        time.sleep(2)
        cur_url = driver.current_url
        expected_url = "http://192.168.10.60:3000/competency-bank/my/"
        if(re.match(expected_url+'[a-zA-Z0-9]', cur_url)):
            body.append(
                f"Competency Title 255 Characters: Pass    {dt_string}")
            assert True
        else:
            body.append(
                f"Competency Title 255 Characters: Fail    {dt_string}")
            assert False

    def test_description255(self):
        driver = self.driver
        time.sleep(2)
        try:
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "title")))
        except:
            driver.get("http://192.168.1.171:3000/competency-bank/add")
        description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "description")))
        save = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/form/div/div[5]/button[2]")))
        title.send_keys(Keys.CONTROL + "a")
        title.send_keys(Keys.DELETE)
        description.send_keys(Keys.CONTROL + "a")
        description.send_keys(Keys.DELETE)
        time.sleep(2)
        title.send_keys(Title)
        description.send_keys(Description255)
        time.sleep(2)
        save.click()
        time.sleep(2)
        cur_url = driver.current_url
        expected_url = "http://192.168.10.60:3000/competency-bank/my"
        if(re.match(expected_url+'[a-zA-Z0-9]', cur_url)):
            body.append(
                f"Competency Description 255 Characters: Pass    {dt_string}")
            assert True
        else:
            body.append(
                f"Competency Description 255 Characters: Fail    {dt_string}")

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
        #     subject = "HRMS-360 System Admin: Competency Functionality"
        #     message = f"subject:{subject}\n\n{body[0]}\n{body[1]}\n{body[2]}\n{body[3]}\n{body[4]}\n{body[5]}\n{body[6]}\n"
        #     smtp.sendmail(sender, receiver, message)
        #     print("Email Sent")
        self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(COMPETENCY_ADMIN("test_BothBlankField"))
    suite.addTest(COMPETENCY_ADMIN("test_BlankTitle"))
    suite.addTest(COMPETENCY_ADMIN("test_BlankDescription"))
    suite.addTest(COMPETENCY_ADMIN("test_title256"))
    suite.addTest(COMPETENCY_ADMIN("test_description256"))
    suite.addTest(COMPETENCY_ADMIN("test_title255"))
    suite.addTest(COMPETENCY_ADMIN("test_description255"))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
    # unittest.main()
