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
Score = 2
negativeScore = -4
Label = "Alpha Testing"
Label255 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer jbmhh"
Label256 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer jbmhht"


class STANDARDRESPONSE(unittest.TestCase):
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
        standardResponse = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/div/div/div/div/div/li[1]")))
        standardResponse.click()
        time.sleep(2)

    def test_blankLabel(self):
        driver = self.driver
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            newResponse = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button"
            )))
            newResponse.click()
            time.sleep(2)
            label = driver.find_element(By.NAME, "label")
            score = driver.find_element(By.NAME, "score")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div/button[2]")
            label.send_keys("")
            score.send_keys(Keys.CONTROL + "a")
            score.send_keys(Keys.DELETE)
            time.sleep(1)
            score.send_keys(Score)
            time.sleep(2)
            save.click()
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Blank label in Standard Response: Fail    {dt_string}")
                assert False
            else:
                cancel = driver.find_element(
                    By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
                cancel.click()
                time.sleep(2)
                body.append(
                    f"Blank label in Standard Response: Pass    {dt_string}")
                assert True

    def test_255Label(self):
        driver = self.driver
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            newResponse = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button"
            )))
            newResponse.click()
            time.sleep(2)
            label = driver.find_element(By.NAME, "label")
            score = driver.find_element(By.NAME, "score")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div/button[2]")
            label.send_keys(Label255)
            score.send_keys(Keys.CONTROL + "a")
            score.send_keys(Keys.DELETE)
            time.sleep(1)
            score.send_keys(Score)
            time.sleep(2)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"255 Characters in Standard Response: Pass    {dt_string}")
                assert True
            else:
                cancel = driver.find_element(
                    By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
                cancel.click()
                time.sleep(2)
                body.append(
                    f"255 Characters in Standard Response: Fail    {dt_string}")
                assert False

    def test_256Label(self):
        driver = self.driver
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            newResponse = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button"
            )))
            newResponse.click()
            time.sleep(2)
            label = driver.find_element(By.NAME, "label")
            score = driver.find_element(By.NAME, "score")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div/button[2]")
            label.send_keys(Label256)
            score.send_keys(Keys.CONTROL + "a")
            score.send_keys(Keys.DELETE)
            time.sleep(1)
            score.send_keys(Score)
            time.sleep(2)
            save.click()
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"256 Characters in Standard Response: Fail    {dt_string}")
                assert False
            else:
                cancel = driver.find_element(
                    By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
                cancel.click()
                time.sleep(2)
                body.append(
                    f"256 Characters in Standard Response: Pass    {dt_string}")
                assert True

    def test_negativeScore(self):
        driver = self.driver
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            newResponse = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button"
            )))
            newResponse.click()
            time.sleep(2)
            label = driver.find_element(By.NAME, "label")
            score = driver.find_element(By.NAME, "score")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div/button[2]")
            label.send_keys(Label)
            score.send_keys(Keys.CONTROL + "a")
            score.send_keys(Keys.DELETE)
            time.sleep(1)
            score.send_keys(negativeScore)
            time.sleep(2)
            save.click()
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(Score < 0 and rows+1 == rows2):
                body.append(
                    f"Negative Score in Standard Response: Fail    {dt_string}")
                assert False
            elif(Score > 0 and rows+1 == rows):
                time.sleep(2)
                body.append(
                    f"Negative Score in Standard Response: Pass    {dt_string}")
                assert True
            else:
                try:
                    cancel = driver.find_element(
                        By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
                    cancel.click()
                    time.sleep(2)
                    body.append(
                        f"Negative Score in Standard Response: Fail    {dt_string}")
                    assert True
                except:
                    time.sleep(2)
                    body.append(
                        f"Negative Score in Standard Response: Fail    {dt_string}")
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
    suite.addTest(STANDARDRESPONSE("test_blankLabel"))
    suite.addTest(STANDARDRESPONSE("test_255Label"))
    suite.addTest(STANDARDRESPONSE("test_256Label"))
    suite.addTest(STANDARDRESPONSE("test_negativeScore"))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
    # unittest.main()
