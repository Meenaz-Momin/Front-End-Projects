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
Name = "Amaan Khan"
Email = "amaan.khan@apsis.com"
Region = "Pune"
Contact = 985631470


class EMPLOYEE(unittest.TestCase):

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
        employee_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/li[4]")))
        employee_tab.click()
        time.sleep(2)

    def test_blankName(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            addEmployee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/div[2]/button[2]"
            )))
            addEmployee.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            region = driver.find_element(By.NAME, "region")
            email = driver.find_element(By.NAME, "email")
            contact = driver.find_element(By.NAME, "contact")
            designation = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[2]/div/div/div/div")
            department = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div")
            lm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[7]/div/div/div/div")
            sm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[8]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[9]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            name.send_keys("")
            region.send_keys(Region)
            email.send_keys(Email)
            contact.send_keys(Contact)
            time.sleep(2)
            action = ActionChains(driver)
            time.sleep(1)
            action.click(designation).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(department).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(lm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(sm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(3)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Name: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(2)
                body.append(f"Blank Name: Pass    {dt_string}")
                assert True

    def test_blankDesignation(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            addEmployee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/div[2]/button[2]"
            )))
            addEmployee.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            region = driver.find_element(By.NAME, "region")
            email = driver.find_element(By.NAME, "email")
            contact = driver.find_element(By.NAME, "contact")
            designation = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[2]/div/div/div/div")
            department = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div")
            lm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[7]/div/div/div/div")
            sm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[8]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[9]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            name.send_keys(Name)
            region.send_keys(Region)
            email.send_keys(Email)
            contact.send_keys(Contact)
            time.sleep(2)
            action = ActionChains(driver)
            time.sleep(1)
            action.click(department).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(lm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(sm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(3)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Designation: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(2)
                body.append(f"Blank Designation: Pass    {dt_string}")
                assert True

    def test_blankDepartment(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            addEmployee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/div[2]/button[2]"
            )))
            addEmployee.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            region = driver.find_element(By.NAME, "region")
            email = driver.find_element(By.NAME, "email")
            contact = driver.find_element(By.NAME, "contact")
            designation = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[2]/div/div/div/div")
            department = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div")
            lm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[7]/div/div/div/div")
            sm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[8]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[9]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            name.send_keys(Name)
            region.send_keys(Region)
            email.send_keys(Email)
            contact.send_keys(Contact)
            time.sleep(2)
            action = ActionChains(driver)
            time.sleep(1)
            action.click(designation).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(lm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(sm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(3)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Department: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(2)
                body.append(f"Blank Department: Pass    {dt_string}")
                assert True

    def test_blankRegion(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            addEmployee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/div[2]/button[2]"
            )))
            addEmployee.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            region = driver.find_element(By.NAME, "region")
            email = driver.find_element(By.NAME, "email")
            contact = driver.find_element(By.NAME, "contact")
            designation = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[2]/div/div/div/div")
            department = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div")
            lm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[7]/div/div/div/div")
            sm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[8]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[9]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            name.send_keys(Name)
            region.send_keys("")
            email.send_keys(Email)
            contact.send_keys(Contact)
            time.sleep(2)
            action = ActionChains(driver)
            time.sleep(1)
            action.click(designation).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(department).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(lm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(sm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(3)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Region: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(2)
                body.append(f"Blank Region: Pass    {dt_string}")
                assert True

    def test_blankEmail(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            addEmployee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/div[2]/button[2]"
            )))
            addEmployee.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            region = driver.find_element(By.NAME, "region")
            email = driver.find_element(By.NAME, "email")
            contact = driver.find_element(By.NAME, "contact")
            designation = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[2]/div/div/div/div")
            department = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div")
            lm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[7]/div/div/div/div")
            sm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[8]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[9]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            name.send_keys(Name)
            region.send_keys(Region)
            email.send_keys("")
            contact.send_keys(Contact)
            time.sleep(2)
            action = ActionChains(driver)
            time.sleep(1)
            action.click(designation).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(department).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(lm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(sm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(3)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Email: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(2)
                body.append(f"Blank Email: Pass    {dt_string}")
                assert True

    def test_blankContact(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            addEmployee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/div[2]/button[2]"
            )))
            addEmployee.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            region = driver.find_element(By.NAME, "region")
            email = driver.find_element(By.NAME, "email")
            contact = driver.find_element(By.NAME, "contact")
            designation = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[2]/div/div/div/div")
            department = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div")
            lm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[7]/div/div/div/div")
            sm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[8]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[9]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            name.send_keys(Name)
            region.send_keys(Region)
            email.send_keys(Email)
            contact.send_keys("")
            time.sleep(2)
            action = ActionChains(driver)
            time.sleep(1)
            action.click(designation).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(department).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(lm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(sm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(3)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Contact: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(2)
                body.append(f"Blank Contact: Pass    {dt_string}")
                assert True

    def test_blankLM(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            addEmployee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/div[2]/button[2]"
            )))
            addEmployee.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            region = driver.find_element(By.NAME, "region")
            email = driver.find_element(By.NAME, "email")
            contact = driver.find_element(By.NAME, "contact")
            designation = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[2]/div/div/div/div")
            department = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div")
            lm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[7]/div/div/div/div")
            sm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[8]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[9]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            name.send_keys(Name)
            region.send_keys(Region)
            email.send_keys(Email)
            contact.send_keys(Contact)
            time.sleep(2)
            action = ActionChains(driver)
            time.sleep(1)
            action.click(designation).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(department).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(sm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(3)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Line Manager: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(2)
                body.append(f"Blank Line Manager: Pass    {dt_string}")
                assert True

    def test_blankSM(self):
        driver = self.driver
        time.sleep(2)
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
        except:
            assert False
        else:
            time.sleep(2)
            addEmployee = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/div[2]/button[2]"
            )))
            addEmployee.click()
            time.sleep(2)
            name = driver.find_element(By.NAME, "name")
            region = driver.find_element(By.NAME, "region")
            email = driver.find_element(By.NAME, "email")
            contact = driver.find_element(By.NAME, "contact")
            designation = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[2]/div/div/div/div")
            department = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[3]/div/div/div/div")
            lm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[7]/div/div/div/div")
            sm = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[8]/div/div/div/div")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[1]/div[9]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            name.send_keys(Name)
            region.send_keys(Region)
            email.send_keys(Email)
            contact.send_keys(Contact)
            time.sleep(2)
            action = ActionChains(driver)
            time.sleep(1)
            action.click(designation).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(department).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(1)
            action.click(lm).perform()
            time.sleep(1)
            action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(3)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Blank Secondary Line Manager: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(2)
                body.append(
                    f"Blank Secondary Line Manager: Pass    {dt_string}")
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
        #     subject = "HRMS-360 Alpha-Testing Employee"
        #     message = f"subject:{subject}\n\n{body[0]}\n{body[1]}\n{body[2]}\n{body[3]}\n{body[4]}\n{body[5]}\n{body[6]}\n{body[7]}\n"
        #     # message = f"subject:{subject}\n\n{body}\n"
        #     smtp.sendmail(sender, receiver, message)
        #     print("Email Sent")
        self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(EMPLOYEE("test_blankName"))
    suite.addTest(EMPLOYEE("test_blankDesignation"))
    suite.addTest(EMPLOYEE("test_blankDepartment"))
    suite.addTest(EMPLOYEE("test_blankRegion"))
    suite.addTest(EMPLOYEE("test_blankEmail"))
    suite.addTest(EMPLOYEE("test_blankContact"))
    suite.addTest(EMPLOYEE("test_blankLM"))
    suite.addTest(EMPLOYEE("test_blankSM"))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
    # unittest.main()
