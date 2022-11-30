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
Company_Name = "Apsis Solutions"
Admin = "Shivani Rajput"
Email = "shivani.rajput@apsissolutions.com"
Start_Date = "24/11/2022"
End_Date = "24/11/2023"
No_Of_Employee = 50
Location = "NIBM, Kondhwa Khurd, Pume-411048"


class TENANT(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.10.60:3000/sign-in")
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
        tenant_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/li[3]")))
        tenant_tab.click()
        time.sleep(2)

    def test_blankCompanyName(self):
        driver = self.driver
        time.sleep(2)
        rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
        ))))
        time.sleep(1)
        add_tenant = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a"
        )))
        add_tenant.click()
        time.sleep(2)
        company_name = driver.find_element(By.NAME, "name")
        location = driver.find_element(By.NAME, "location")
        employee_base = driver.find_element(By.NAME, "no_of_employee")
        admin = driver.find_element(By.NAME, "admin_name")
        admin_mail = driver.find_element(By.NAME, "email")
        approval = driver.find_element(By.NAME, "is_lm_approval_required")
        start_date = driver.find_element(By.NAME, "start_date")
        end_date = driver.find_element(By.NAME, "end_date")
        status = driver.find_element(By.NAME, "is_active")
        industry = driver.find_element(
            By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
        type1 = driver.find_element(By.XPATH, "//input[@value='on premise']")
        type2 = driver.find_element(
            By.XPATH, "//input[@value='channel partner']")
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
        back = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]/div")
        company_name.send_keys("")
        time.sleep(1)
        location.send_keys(Location)
        time.sleep(1)
        employee_base.send_keys(No_Of_Employee)
        time.sleep(1)
        admin.send_keys(Admin)
        time.sleep(1)
        admin_mail.send_keys(Email)
        time.sleep(1)
        approval.click()
        time.sleep(1)
        start_date.send_keys(Start_Date)
        time.sleep(1)
        end_date.send_keys(End_Date)
        time.sleep(1)
        status.click()
        time.sleep(1)
        type1.click()
        time.sleep(1)
        action = ActionChains(driver)
        action.click(industry).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        save.click()
        time.sleep(2)
        try:
            rows2 = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Company Name: Fail    {dt_string}")
                assert False
            else:
                body.append(f"blank Company Name: Pass    {dt_string}")
                assert True
        except:
            back.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Company Name: Fail    {dt_string}")
                assert False
            else:
                body.append(f"blank Company Name: Pass    {dt_string}")
                assert True

    def test_blankLocation(self):
        driver = self.driver
        time.sleep(2)
        rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
        ))))
        time.sleep(1)
        add_tenant = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a"
        )))
        add_tenant.click()
        time.sleep(2)
        company_name = driver.find_element(By.NAME, "name")
        location = driver.find_element(By.NAME, "location")
        employee_base = driver.find_element(By.NAME, "no_of_employee")
        admin = driver.find_element(By.NAME, "admin_name")
        admin_mail = driver.find_element(By.NAME, "email")
        approval = driver.find_element(By.NAME, "is_lm_approval_required")
        start_date = driver.find_element(By.NAME, "start_date")
        end_date = driver.find_element(By.NAME, "end_date")
        status = driver.find_element(By.NAME, "is_active")
        industry = driver.find_element(
            By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
        type1 = driver.find_element(By.XPATH, "//input[@value='on premise']")
        type2 = driver.find_element(
            By.XPATH, "//input[@value='channel partner']")
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
        back = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]/div")
        company_name.send_keys(Company_Name)
        time.sleep(1)
        location.send_keys("")
        time.sleep(1)
        employee_base.send_keys(No_Of_Employee)
        time.sleep(1)
        admin.send_keys(Admin)
        time.sleep(1)
        admin_mail.send_keys(Email)
        time.sleep(1)
        approval.click()
        time.sleep(1)
        start_date.send_keys(Start_Date)
        time.sleep(1)
        end_date.send_keys(End_Date)
        time.sleep(1)
        status.click()
        time.sleep(1)
        type1.click()
        time.sleep(1)
        action = ActionChains(driver)
        action.click(industry).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        save.click()
        time.sleep(2)
        try:
            rows2 = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Company Name: Fail    {dt_string}")
                assert False
            else:
                body.append(f"blank Company Name: Pass    {dt_string}")
                assert True
        except:
            back.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Company Name: Fail    {dt_string}")
                assert False
            else:
                body.append(f"blank Company Name: Pass    {dt_string}")
                assert True

    def test_blankIndustryName(self):
        driver = self.driver
        time.sleep(2)
        rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
        ))))
        time.sleep(1)
        add_tenant = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a"
        )))
        add_tenant.click()
        time.sleep(2)
        company_name = driver.find_element(By.NAME, "name")
        location = driver.find_element(By.NAME, "location")
        employee_base = driver.find_element(By.NAME, "no_of_employee")
        admin = driver.find_element(By.NAME, "admin_name")
        admin_mail = driver.find_element(By.NAME, "email")
        approval = driver.find_element(By.NAME, "is_lm_approval_required")
        start_date = driver.find_element(By.NAME, "start_date")
        end_date = driver.find_element(By.NAME, "end_date")
        status = driver.find_element(By.NAME, "is_active")
        industry = driver.find_element(
            By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
        type1 = driver.find_element(By.XPATH, "//input[@value='on premise']")
        type2 = driver.find_element(
            By.XPATH, "//input[@value='channel partner']")
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
        back = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]/div")
        company_name.send_keys(Company_Name)
        time.sleep(1)
        location.send_keys(Location)
        time.sleep(1)
        employee_base.send_keys(No_Of_Employee)
        time.sleep(1)
        admin.send_keys(Admin)
        time.sleep(1)
        admin_mail.send_keys(Email)
        time.sleep(1)
        approval.click()
        time.sleep(1)
        start_date.send_keys(Start_Date)
        time.sleep(1)
        end_date.send_keys(End_Date)
        time.sleep(1)
        status.click()
        time.sleep(1)
        type1.click()
        time.sleep(1)
        # action = ActionChains(driver)
        # action.click(industry).perform()
        # action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        save.click()
        time.sleep(2)
        try:
            rows2 = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Industry Name: Fail    {dt_string}")
                assert False
            else:
                body.append(f"blank Industry Name: Pass    {dt_string}")
                assert True
        except:
            back.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Industry Name: Fail    {dt_string}")
                assert False
            else:
                body.append(f"blank Industry Name: Pass    {dt_string}")
                assert True

    def test_EmployeeBaseZero(self):
        driver = self.driver
        time.sleep(2)
        rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
        ))))
        time.sleep(1)
        add_tenant = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a"
        )))
        add_tenant.click()
        time.sleep(2)
        company_name = driver.find_element(By.NAME, "name")
        location = driver.find_element(By.NAME, "location")
        employee_base = driver.find_element(By.NAME, "no_of_employee")
        admin = driver.find_element(By.NAME, "admin_name")
        admin_mail = driver.find_element(By.NAME, "email")
        approval = driver.find_element(By.NAME, "is_lm_approval_required")
        start_date = driver.find_element(By.NAME, "start_date")
        end_date = driver.find_element(By.NAME, "end_date")
        status = driver.find_element(By.NAME, "is_active")
        industry = driver.find_element(
            By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
        type1 = driver.find_element(By.XPATH, "//input[@value='on premise']")
        type2 = driver.find_element(
            By.XPATH, "//input[@value='channel partner']")
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
        back = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]/div")
        company_name.send_keys(Company_Name)
        time.sleep(1)
        location.send_keys(Location)
        time.sleep(1)
        admin.send_keys(Admin)
        time.sleep(1)
        admin_mail.send_keys(Email)
        time.sleep(1)
        approval.click()
        time.sleep(1)
        start_date.send_keys(Start_Date)
        time.sleep(1)
        end_date.send_keys(End_Date)
        time.sleep(1)
        status.click()
        time.sleep(1)
        type1.click()
        time.sleep(1)
        action = ActionChains(driver)
        action.click(industry).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        save.click()
        time.sleep(2)
        try:
            rows2 = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Employee Base Zero: Fail    {dt_string}")
                assert False
            else:
                body.append(f"Employee Base Zero: Pass    {dt_string}")
                assert True
        except:
            back.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Employee Base Zero: Fail    {dt_string}")
                assert False
            else:
                body.append(f"Employee Base Zero: Pass    {dt_string}")
                assert True

    def test_blankAdminName(self):
        driver = self.driver
        time.sleep(2)
        rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
        ))))
        time.sleep(1)
        add_tenant = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a"
        )))
        add_tenant.click()
        time.sleep(2)
        company_name = driver.find_element(By.NAME, "name")
        location = driver.find_element(By.NAME, "location")
        employee_base = driver.find_element(By.NAME, "no_of_employee")
        admin = driver.find_element(By.NAME, "admin_name")
        admin_mail = driver.find_element(By.NAME, "email")
        approval = driver.find_element(By.NAME, "is_lm_approval_required")
        start_date = driver.find_element(By.NAME, "start_date")
        end_date = driver.find_element(By.NAME, "end_date")
        status = driver.find_element(By.NAME, "is_active")
        industry = driver.find_element(
            By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
        type1 = driver.find_element(By.XPATH, "//input[@value='on premise']")
        type2 = driver.find_element(
            By.XPATH, "//input[@value='channel partner']")
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
        back = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]/div")
        company_name.send_keys(Company_Name)
        time.sleep(1)
        location.send_keys(Location)
        time.sleep(1)
        employee_base.send_keys(No_Of_Employee)
        time.sleep(1)
        admin.send_keys("")
        time.sleep(1)
        admin_mail.send_keys(Email)
        time.sleep(1)
        approval.click()
        time.sleep(1)
        start_date.send_keys(Start_Date)
        time.sleep(1)
        end_date.send_keys(End_Date)
        time.sleep(1)
        status.click()
        time.sleep(1)
        type1.click()
        time.sleep(1)
        action = ActionChains(driver)
        action.click(industry).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        save.click()
        time.sleep(2)
        try:
            rows2 = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Admin Name: Fail    {dt_string}")
                assert False
            else:
                body.append(f"blank Admin Name: Pass    {dt_string}")
                assert True
        except:
            back.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Admin Name: Fail    {dt_string}")
                assert False
            else:
                body.append(f"blank Admin Name: Pass    {dt_string}")
                assert True

    def test_blankAdminEmail(self):
        driver = self.driver
        time.sleep(2)
        rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
        ))))
        time.sleep(1)
        add_tenant = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a"
        )))
        add_tenant.click()
        time.sleep(2)
        company_name = driver.find_element(By.NAME, "name")
        location = driver.find_element(By.NAME, "location")
        employee_base = driver.find_element(By.NAME, "no_of_employee")
        admin = driver.find_element(By.NAME, "admin_name")
        admin_mail = driver.find_element(By.NAME, "email")
        approval = driver.find_element(By.NAME, "is_lm_approval_required")
        start_date = driver.find_element(By.NAME, "start_date")
        end_date = driver.find_element(By.NAME, "end_date")
        status = driver.find_element(By.NAME, "is_active")
        industry = driver.find_element(
            By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
        type1 = driver.find_element(By.XPATH, "//input[@value='on premise']")
        type2 = driver.find_element(
            By.XPATH, "//input[@value='channel partner']")
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
        back = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]/div")
        company_name.send_keys(Company_Name)
        time.sleep(1)
        location.send_keys(Location)
        time.sleep(1)
        employee_base.send_keys(No_Of_Employee)
        time.sleep(1)
        admin.send_keys(Admin)
        time.sleep(1)
        admin_mail.send_keys("")
        time.sleep(1)
        approval.click()
        time.sleep(1)
        start_date.send_keys(Start_Date)
        time.sleep(1)
        end_date.send_keys(End_Date)
        time.sleep(1)
        status.click()
        time.sleep(1)
        type1.click()
        time.sleep(1)
        action = ActionChains(driver)
        action.click(industry).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        save.click()
        time.sleep(2)
        try:
            rows2 = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Admin Email: Fail    {dt_string}")
                assert False
            else:
                body.append(f"blank Admin Email: Pass    {dt_string}")
                assert True
        except:
            back.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Admin Email: Fail    {dt_string}")
                assert False
            else:
                body.append(f"blank Admin Email: Pass    {dt_string}")
                assert True

    def test_diableApproval(self):
        driver = self.driver
        time.sleep(2)
        rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
        ))))
        time.sleep(1)
        add_tenant = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a"
        )))
        add_tenant.click()
        time.sleep(2)
        company_name = driver.find_element(By.NAME, "name")
        location = driver.find_element(By.NAME, "location")
        employee_base = driver.find_element(By.NAME, "no_of_employee")
        admin = driver.find_element(By.NAME, "admin_name")
        admin_mail = driver.find_element(By.NAME, "email")
        approval = driver.find_element(By.NAME, "is_lm_approval_required")
        start_date = driver.find_element(By.NAME, "start_date")
        end_date = driver.find_element(By.NAME, "end_date")
        status = driver.find_element(By.NAME, "is_active")
        industry = driver.find_element(
            By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
        type1 = driver.find_element(By.XPATH, "//input[@value='on premise']")
        type2 = driver.find_element(
            By.XPATH, "//input[@value='channel partner']")
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
        back = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]/div")
        company_name.send_keys(Company_Name)
        time.sleep(1)
        location.send_keys(Location)
        time.sleep(1)
        employee_base.send_keys(No_Of_Employee)
        time.sleep(1)
        admin.send_keys(Admin)
        time.sleep(1)
        admin_mail.send_keys(Email)
        time.sleep(1)
        start_date.send_keys(Start_Date)
        time.sleep(1)
        end_date.send_keys(End_Date)
        time.sleep(1)
        status.click()
        time.sleep(1)
        type1.click()
        time.sleep(1)
        action = ActionChains(driver)
        action.click(industry).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        save.click()
        time.sleep(2)
        try:
            rows2 = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Disable Line Manager Approval: Pass    {dt_string}")
                assert True
            else:
                body.append(
                    f"Disable Line Manager Approval: Fail    {dt_string}")
                assert False
        except:
            back.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Disable Line Manager Approval: Pass    {dt_string}")
                assert True
            else:
                body.append(
                    f"Disable Line Manager Approval: Fail    {dt_string}")
                assert False

    def test_NotSelectAdminType(self):
        driver = self.driver
        time.sleep(2)
        rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
        ))))
        time.sleep(1)
        add_tenant = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a"
        )))
        add_tenant.click()
        time.sleep(2)
        company_name = driver.find_element(By.NAME, "name")
        location = driver.find_element(By.NAME, "location")
        employee_base = driver.find_element(By.NAME, "no_of_employee")
        admin = driver.find_element(By.NAME, "admin_name")
        admin_mail = driver.find_element(By.NAME, "email")
        approval = driver.find_element(By.NAME, "is_lm_approval_required")
        start_date = driver.find_element(By.NAME, "start_date")
        end_date = driver.find_element(By.NAME, "end_date")
        status = driver.find_element(By.NAME, "is_active")
        industry = driver.find_element(
            By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
        type1 = driver.find_element(By.XPATH, "//input[@value='on premise']")
        type2 = driver.find_element(
            By.XPATH, "//input[@value='channel partner']")
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
        back = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]/div")
        company_name.send_keys(Company_Name)
        time.sleep(1)
        location.send_keys(Location)
        time.sleep(1)
        employee_base.send_keys(No_Of_Employee)
        time.sleep(1)
        admin.send_keys(Admin)
        time.sleep(1)
        admin_mail.send_keys(Email)
        time.sleep(1)
        approval.click()
        time.sleep(1)
        start_date.send_keys(Start_Date)
        time.sleep(1)
        end_date.send_keys(End_Date)
        time.sleep(1)
        status.click()
        time.sleep(1)
        action = ActionChains(driver)
        action.click(industry).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        save.click()
        time.sleep(2)
        try:
            rows2 = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Not selected any admin type: Fail    {dt_string}")
                assert False
            else:
                body.append(
                    f"Not selected any admin type: Pass    {dt_string}")
                assert True
        except:
            back.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Not selected any admin type: Fail    {dt_string}")
                assert False
            else:
                body.append(
                    f"Not selected any admin type: Pass    {dt_string}")
                assert True

    def test_blankStartDate(self):
        driver = self.driver
        time.sleep(2)
        rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
        ))))
        time.sleep(1)
        add_tenant = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a"
        )))
        add_tenant.click()
        time.sleep(2)
        company_name = driver.find_element(By.NAME, "name")
        location = driver.find_element(By.NAME, "location")
        employee_base = driver.find_element(By.NAME, "no_of_employee")
        admin = driver.find_element(By.NAME, "admin_name")
        admin_mail = driver.find_element(By.NAME, "email")
        approval = driver.find_element(By.NAME, "is_lm_approval_required")
        start_date = driver.find_element(By.NAME, "start_date")
        end_date = driver.find_element(By.NAME, "end_date")
        status = driver.find_element(By.NAME, "is_active")
        industry = driver.find_element(
            By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
        type1 = driver.find_element(By.XPATH, "//input[@value='on premise']")
        type2 = driver.find_element(
            By.XPATH, "//input[@value='channel partner']")
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
        back = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]/div")
        company_name.send_keys(Company_Name)
        time.sleep(1)
        location.send_keys(Location)
        time.sleep(1)
        employee_base.send_keys(No_Of_Employee)
        time.sleep(1)
        admin.send_keys(Admin)
        time.sleep(1)
        admin_mail.send_keys(Email)
        time.sleep(1)
        approval.click()
        time.sleep(1)
        start_date.send_keys("")
        time.sleep(1)
        end_date.send_keys(End_Date)
        time.sleep(1)
        status.click()
        time.sleep(1)
        type1.click()
        time.sleep(1)
        action = ActionChains(driver)
        action.click(industry).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        save.click()
        time.sleep(2)
        try:
            rows2 = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Start Date: Fail    {dt_string}")
                assert False
            else:
                body.append(f"Blank Start Date: Pass    {dt_string}")
                assert True
        except:
            back.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank Start Date: Fail    {dt_string}")
                assert False
            else:
                body.append(f"Blank Start Date: Pass    {dt_string}")
                assert True

    def test_blankEndDate(self):
        driver = self.driver
        time.sleep(2)
        rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
        ))))
        time.sleep(1)
        add_tenant = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a"
        )))
        add_tenant.click()
        time.sleep(2)
        company_name = driver.find_element(By.NAME, "name")
        location = driver.find_element(By.NAME, "location")
        employee_base = driver.find_element(By.NAME, "no_of_employee")
        admin = driver.find_element(By.NAME, "admin_name")
        admin_mail = driver.find_element(By.NAME, "email")
        approval = driver.find_element(By.NAME, "is_lm_approval_required")
        start_date = driver.find_element(By.NAME, "start_date")
        end_date = driver.find_element(By.NAME, "end_date")
        status = driver.find_element(By.NAME, "is_active")
        industry = driver.find_element(
            By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
        type1 = driver.find_element(By.XPATH, "//input[@value='on premise']")
        type2 = driver.find_element(
            By.XPATH, "//input[@value='channel partner']")
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
        back = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]/div")
        company_name.send_keys(Company_Name)
        time.sleep(1)
        location.send_keys(Location)
        time.sleep(1)
        employee_base.send_keys(No_Of_Employee)
        time.sleep(1)
        admin.send_keys(Admin)
        time.sleep(1)
        admin_mail.send_keys(Email)
        time.sleep(1)
        approval.click()
        time.sleep(1)
        start_date.send_keys(Start_Date)
        time.sleep(1)
        end_date.send_keys("")
        time.sleep(1)
        status.click()
        time.sleep(1)
        type1.click()
        time.sleep(1)
        action = ActionChains(driver)
        action.click(industry).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        save.click()
        time.sleep(2)
        try:
            rows2 = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank End Date: Fail    {dt_string}")
                assert False
            else:
                body.append(f"Blank End Date: Pass    {dt_string}")
                assert True
        except:
            back.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(f"Blank End Date: Fail    {dt_string}")
                assert False
            else:
                body.append(f"Blank End Date: Pass    {dt_string}")
                assert True

    def test_disableStatus(self):
        driver = self.driver
        time.sleep(2)
        rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
        ))))
        time.sleep(1)
        add_tenant = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/a"
        )))
        add_tenant.click()
        time.sleep(2)
        company_name = driver.find_element(By.NAME, "name")
        location = driver.find_element(By.NAME, "location")
        employee_base = driver.find_element(By.NAME, "no_of_employee")
        admin = driver.find_element(By.NAME, "admin_name")
        admin_mail = driver.find_element(By.NAME, "email")
        approval = driver.find_element(By.NAME, "is_lm_approval_required")
        start_date = driver.find_element(By.NAME, "start_date")
        end_date = driver.find_element(By.NAME, "end_date")
        status = driver.find_element(By.NAME, "is_active")
        industry = driver.find_element(
            By.XPATH, "//*[@id='panel1bh-content']/div/div/div[3]/div/div/div/div")
        type1 = driver.find_element(By.XPATH, "//input[@value='on premise']")
        type2 = driver.find_element(
            By.XPATH, "//input[@value='channel partner']")
        save = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[4]/button[2]")
        back = driver.find_element(
            By.XPATH, "//*[@id='__next']/div[1]/header/div/div/div[1]/div")
        company_name.send_keys(Company_Name)
        time.sleep(1)
        location.send_keys(Location)
        time.sleep(1)
        employee_base.send_keys(No_Of_Employee)
        time.sleep(1)
        admin.send_keys(Admin)
        time.sleep(1)
        admin_mail.send_keys(Email)
        time.sleep(1)
        approval.click()
        time.sleep(1)
        start_date.send_keys(Start_Date)
        time.sleep(1)
        end_date.send_keys(End_Date)
        time.sleep(1)
        status.click()
        time.sleep(1)
        type1.click()
        time.sleep(1)
        action = ActionChains(driver)
        action.click(industry).perform()
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        save.click()
        time.sleep(2)
        try:
            rows2 = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Disable subscription Status: Pass    {dt_string}")
                assert True
            else:
                body.append(
                    f"Disable subscription Status: Fail    {dt_string}")
                assert False
        except:
            back.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"
            ))))
            if(rows+1 == rows2):
                body.append(
                    f"Disable subscription Status: Pass    {dt_string}")
                assert True
            else:
                body.append(
                    f"Disable subscription Status: Fail    {dt_string}")
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
        #     subject = "HRMS-360 System Admin: Create TENANT"
        #     # message = f"subject:{subject}\n\n{body}\n"
        #     message = f"subject:{subject}\n\n{body[0]}\n{body[1]}\n{body[2]}\n{body[3]}\n{body[4]}\n{body[5]}\n{body[6]}\n{body[7]}\n{body[8]}\n{body[9]}\n{body[10]}\n{body[11]}\n"
        #     smtp.sendmail(sender, receiver, message)
        #     print("Email Sent")
        self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TENANT("test_blankCompanyName"))
    suite.addTest(TENANT("test_blankLocation"))
    suite.addTest(TENANT("test_blankIndustryName"))
    suite.addTest(TENANT("test_EmployeeBaseZero"))
    suite.addTest(TENANT("test_blankAdminName"))
    suite.addTest(TENANT("test_blankAdminEmail"))
    suite.addTest(TENANT("test_blankAdminEmail"))
    suite.addTest(TENANT("test_diableApproval"))
    suite.addTest(TENANT("test_NotSelectAdminType"))
    suite.addTest(TENANT("test_blankStartDate"))
    suite.addTest(TENANT("test_blankEndDate"))
    suite.addTest(TENANT("test_disableStatus"))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
    # unittest.main()
