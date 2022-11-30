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
valid_mail = "channel.partner@apsis.com"
valid_password = "1234"
Question = "Alpha Testing"
Question256 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer eget abhy"
Question255 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer egetv"


class QUESTIONS_ADMIN(unittest.TestCase):

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
        edit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/button[2]"
        )))
        edit.click()
        time.sleep(2)
        questions = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/div/button[2]"
        )))
        questions.click()
        time.sleep(2)

    def test_blankQuestion(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
        except:
            assert False
        else:
            newQuestion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button"
            )))
            newQuestion.click()
            time.sleep(2)
            question = driver.find_element(By.NAME, "text")
            area_assessed = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
            response_type = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            question.send_keys("")
            action = ActionChains(driver)
            action.click(area_assessed).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(response_type).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(2)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Field in Question: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(2)
                body.append(f"Blank Field in Question: Pass    {dt_string}")
                assert True

    def test_255Question(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
        except:
            assert False
        else:
            newQuestion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button"
            )))
            newQuestion.click()
            time.sleep(2)
            question = driver.find_element(By.NAME, "text")
            area_assessed = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
            response_type = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            question.send_keys(Question255)
            time.sleep(2)
            action = ActionChains(driver)
            action.click(area_assessed).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(response_type).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(2)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"255 Character in Question: Pass    {dt_string}")
                assert True
            else:
                cancel.click()
                time.sleep(2)
                body.append(f"255 Character in Question: Fail    {dt_string}")
                assert False

    def test_256Question(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
        except:
            assert False
        else:
            newQuestion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button"
            )))
            newQuestion.click()
            time.sleep(2)
            question = driver.find_element(By.NAME, "text")
            area_assessed = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
            response_type = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            question.send_keys(Question256)
            time.sleep(2)
            action = ActionChains(driver)
            action.click(area_assessed).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(response_type).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(2)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"256 Character in Question: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(2)
                body.append(f"256 Character in Question: Pass    {dt_string}")
                assert True

    def test_blankAssessment(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
        except:
            assert False
        else:
            newQuestion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button"
            )))
            newQuestion.click()
            time.sleep(2)
            question = driver.find_element(By.NAME, "text")
            area_assessed = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
            response_type = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            question.send_keys(Question)
            time.sleep(2)
            action = ActionChains(driver)
            time.sleep(1)
            action.click(response_type).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(2)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Blank Field in Area Assessed: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(2)
                body.append(
                    f"Blank Field in Area Assessed: Pass    {dt_string}")
                assert True

    def test_allAssessment(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
        except:
            assert False
        else:
            newQuestion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button"
            )))
            newQuestion.click()
            time.sleep(2)
            question = driver.find_element(By.NAME, "text")
            area_assessed = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
            response_type = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            question.send_keys(Question)
            time.sleep(2)
            action = ActionChains(driver)
            time.sleep(1)
            for i in range(0, 8):
                action.click(area_assessed).perform()
                action.send_keys(Keys.ARROW_DOWN).send_keys(
                    Keys.ENTER).perform()
                time.sleep(2)
            action.click(response_type).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(2)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"All Area Assessed: Pass    {dt_string}")
                assert True
            else:
                cancel.click()
                time.sleep(2)
                body.append(
                    f"All Area Assessed: Fail    {dt_string}")
                assert False

    def test_blankResponseType(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
        except:
            assert False
        else:
            newQuestion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button"
            )))
        newQuestion.click()
        time.sleep(2)
        question = driver.find_element(By.NAME, "text")
        area_assessed = driver.find_element(
            By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
        response_type = driver.find_element(
            By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
        save = driver.find_element(
            By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
        cancel = driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
        question.send_keys(Question)
        time.sleep(2)
        action = ActionChains(driver)
        action.click(area_assessed).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(1)
        time.sleep(2)
        save.click()
        time.sleep(2)
        rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
        ))))
        if(rows+1 == rows2):
            body.append(
                f"Blank Field in Response Type: Fail    {dt_string}")
            assert False
        else:
            cancel.click()
            time.sleep(2)
            body.append(
                f"Blank Field in Response Type: Pass    {dt_string}")
            assert True

    def test_textResponse(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
        except:
            assert False
        else:
            newQuestion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button"
            )))
            newQuestion.click()
            time.sleep(2)
            question = driver.find_element(By.NAME, "text")
            area_assessed = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
            response_type = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            question.send_keys(Question)
            time.sleep(2)
            action = ActionChains(driver)
            action.click(area_assessed).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(response_type).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(2)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Text in response Type: Pass    {dt_string}")
                assert True
            else:
                cancel.click()
                time.sleep(2)
                body.append(
                    f"Text in response Type: Fail    {dt_string}")
                assert False

    def test_yes_noResponse(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
        except:
            assert False
        else:
            newQuestion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button"
            )))
            newQuestion.click()
            time.sleep(2)
            question = driver.find_element(By.NAME, "text")
            area_assessed = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
            response_type = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            question.send_keys(Question)
            action = ActionChains(driver)
            action.click(area_assessed).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(response_type).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(
                Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(2)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Yes/No in response Type: Pass    {dt_string}")
                assert True
            else:
                cancel.click()
                time.sleep(2)
                body.append(
                    f"Yes/No in response Type: Fail    {dt_string}")
                assert False

    def test_MCQResponse(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
        except:
            assert False
        else:
            newQuestion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button"
            )))
            newQuestion.click()
            time.sleep(2)
            question = driver.find_element(By.NAME, "text")
            area_assessed = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
            response_type = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            question.send_keys(Question)
            action = ActionChains(driver)
            action.click(area_assessed).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(response_type).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(
                Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(2)
            label1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.0.label")))
            label1.send_keys("first")
            time.sleep(1)
            label2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.1.label")))
            label2.send_keys("second")
            time.sleep(1)
            add_other = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[2]/ul[1]/li[3]/p[1]/span[1]"))
            )
            add_other.click()
            time.sleep(1)
            label3 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.2.label")))
            label3.send_keys("third")
            time.sleep(1)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"MCQ response Type: Pass    {dt_string}")
                assert True
            else:
                cancel.click()
                time.sleep(2)
                body.append(
                    f"MCQ response Type: Fail    {dt_string}")
                assert False

    def test_MultipleMCQResponse(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
        except:
            assert False
        else:
            newQuestion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button"
            )))
            newQuestion.click()
            time.sleep(2)
            question = driver.find_element(By.NAME, "text")
            area_assessed = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
            response_type = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            question.send_keys(Question)
            action = ActionChains(driver)
            action.click(area_assessed).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(response_type).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(
                Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(2)
            label1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.0.label")))
            label1.send_keys("first")
            time.sleep(1)
            label2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.1.label")))
            label2.send_keys("second")
            time.sleep(1)
            add_other = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[2]/ul[1]/li[3]/p[1]/span[1]"))
            )
            add_other.click()
            time.sleep(1)
            label3 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.2.label")))
            label3.send_keys("third")
            time.sleep(1)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Multiple MCQ response Type: Pass    {dt_string}")
                assert True
            else:
                cancel.click()
                time.sleep(2)
                body.append(
                    f"Multiple MCQ response Type: Fail    {dt_string}")
                assert False

    def test_LikertResponse(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
        except:
            assert False
        else:
            newQuestion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[1]/button"
            )))
            newQuestion.click()
            time.sleep(2)
            question = driver.find_element(By.NAME, "text")
            area_assessed = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/div/div")
            response_type = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[4]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            question.send_keys(Question)
            action = ActionChains(driver)
            action.click(area_assessed).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(response_type).perform()
            action.send_keys(Keys.ARROW_DOWN).send_keys(
                Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(2)
            label1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.0.label")))
            score1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.0.score")))
            label1.send_keys("Agree")
            score1.send_keys(1)
            time.sleep(1)
            label2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.1.label")))
            score2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.1.score")))
            label2.send_keys("Neutral")
            score2.send_keys(2)
            time.sleep(1)
            add_other = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[2]/ul[1]/li[3]/p[1]/span[1]"))
            )
            add_other.click()
            time.sleep(1)
            label3 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.2.label")))
            score3 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "responses.2.score")))
            label3.send_keys("Disagree")
            score3.send_keys(3)
            time.sleep(1)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Likert Scale response Type: Pass    {dt_string}")
                assert True
            else:
                cancel.click()
                time.sleep(2)
                body.append(
                    f"Likert Scale response Type: Fail    {dt_string}")
                assert False

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
        #     subject = "HRMS-360 System Admin: Create Questions"
        #     # message = f"subject:{subject}\n\n{body}\n"
        #     message = f"subject:{subject}\n\n{body[0]}\n{body[1]}\n{body[2]}\n{body[3]}\n{body[4]}\n{body[5]}\n{body[6]}\n{body[7]}\n{body[8]}\n{body[9]}\n{body[10]}\n"
        #     smtp.sendmail(sender, receiver, message)
        #     print("Email Sent")
        self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(QUESTIONS_ADMIN("test_blankQuestion"))
    suite.addTest(QUESTIONS_ADMIN("test_255Question"))
    suite.addTest(QUESTIONS_ADMIN("test_256Question"))
    suite.addTest(QUESTIONS_ADMIN("test_blankAssessment"))
    suite.addTest(QUESTIONS_ADMIN("test_allAssessment"))
    suite.addTest(QUESTIONS_ADMIN("test_blankResponseType"))
    suite.addTest(QUESTIONS_ADMIN("test_textResponse"))
    suite.addTest(QUESTIONS_ADMIN("test_yes_noResponse"))
    suite.addTest(QUESTIONS_ADMIN("test_MCQResponse"))
    suite.addTest(QUESTIONS_ADMIN("test_MultipleMCQResponse"))
    suite.addTest(QUESTIONS_ADMIN("test_LikertResponse"))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
    # unittest.main()
