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
Category = "Alpha Testing"
Category255 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer jbmhh"
Category256 = "tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer jbmhht"
No_of_rater = 2
Negative_no = -3


class RATERS(unittest.TestCase):
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
        raters = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/div/div/div/div/div/li[5]")))
        raters.click()
        time.sleep(2)

    def test_blankCategory(self):
        time.sleep(2)
        driver = self.driver
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newCategory = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button"
            )))
            newCategory.click()
            time.sleep(2)
            category = driver.find_element(By.NAME, "category_name")
            no_of_rater = driver.find_element(By.NAME, "no_of_raters")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[5]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            category.send_keys("")
            no_of_rater.send_keys(Keys.CONTROL + "a")
            no_of_rater.send_keys(Keys.DELETE)
            time.sleep(1)
            no_of_rater.send_keys(No_of_rater)
            time.sleep(1)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))

            if(rows+1 == rows2):
                body.append(
                    f"Blank Field in Rater Category: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(1)
                body.append(
                    f"Blank Field in Rater Category: Pass    {dt_string}")
                assert True

    def test_255Category(self):
        time.sleep(2)
        driver = self.driver
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newCategory = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button"
            )))
            newCategory.click()
            time.sleep(2)
            category = driver.find_element(By.NAME, "category_name")
            no_of_rater = driver.find_element(By.NAME, "no_of_raters")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[5]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            category.send_keys(Category255)
            no_of_rater.send_keys(Keys.CONTROL + "a")
            no_of_rater.send_keys(Keys.DELETE)
            time.sleep(1)
            no_of_rater.send_keys(No_of_rater)
            time.sleep(1)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))

            if(rows+1 == rows2):
                body.append(
                    f"255 Characters in Rater Category: Pass    {dt_string}")
                assert True
            else:
                cancel.click()
                time.sleep(1)
                body.append(
                    f"255 Characters in Rater Category: Fail    {dt_string}")
                assert False

    def test_256Category(self):
        time.sleep(2)
        driver = self.driver
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newCategory = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button"
            )))
            newCategory.click()
            time.sleep(2)
            category = driver.find_element(By.NAME, "category_name")
            no_of_rater = driver.find_element(By.NAME, "no_of_raters")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[5]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            category.send_keys(Category256)
            no_of_rater.send_keys(Keys.CONTROL + "a")
            no_of_rater.send_keys(Keys.DELETE)
            time.sleep(1)
            no_of_rater.send_keys(No_of_rater)
            time.sleep(1)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
            if(rows+1 == rows2):
                body.append(
                    f"256 Characters in Rater Category: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(1)
                body.append(
                    f"256 Characetrs in Blank Field in Rater Category: Pass    {dt_string}")
                assert True

    def test_negativeRaters(self):
        time.sleep(2)
        driver = self.driver
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newCategory = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button"
            )))
            newCategory.click()
            time.sleep(2)
            category = driver.find_element(By.NAME, "category_name")
            no_of_rater = driver.find_element(By.NAME, "no_of_raters")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[5]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            category.send_keys(Category)
            no_of_rater.send_keys(Keys.CONTROL + "a")
            no_of_rater.send_keys(Keys.DELETE)
            time.sleep(1)
            no_of_rater.send_keys(Negative_no)
            time.sleep(1)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))

            if(rows+1 == rows2):
                body.append(
                    f"Negative No of Raters in Rater Category: Fail    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(1)
                body.append(
                    f"Negative no of in Rater Category: Pass    {dt_string}")
                assert True

    def test_bothSwitchOn(self):
        time.sleep(2)
        driver = self.driver
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newCategory = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button"
            )))
            newCategory.click()
            time.sleep(2)
            category = driver.find_element(By.NAME, "category_name")
            no_of_rater = driver.find_element(By.NAME, "no_of_raters")
            is_mandatory = driver.find_element(By.NAME, "is_required")
            is_external = driver.find_element(By.NAME, "is_external")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[5]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            category.send_keys(Category)
            no_of_rater.send_keys(Keys.CONTROL + "a")
            no_of_rater.send_keys(Keys.DELETE)
            time.sleep(1)
            no_of_rater.send_keys(No_of_rater)
            is_external.click()
            time.sleep(1)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))

            if(rows+1 == rows2):
                body.append(
                    f"Both Switches on in Rater Category: Pass    {dt_string}")
                assert False
            else:
                cancel.click()
                time.sleep(1)
                body.append(
                    f"Both Switches on in Rater Category: Fail    {dt_string}")
                assert True

    def test_bothSwitchOff(self):
        time.sleep(2)
        driver = self.driver
        try:
            rows = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))
        except:
            assert False
        else:
            newCategory = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[1]/button"
            )))
            newCategory.click()
            time.sleep(2)
            category = driver.find_element(By.NAME, "category_name")
            no_of_rater = driver.find_element(By.NAME, "no_of_raters")
            is_mandatory = driver.find_element(By.NAME, "is_required")
            is_external = driver.find_element(By.NAME, "is_external")
            save = driver.find_element(
                By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/form/div/div[5]/div/button[2]")
            cancel = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[1]/div[1]/h2[1]/button[1]")
            category.send_keys(Category)
            no_of_rater.send_keys(Keys.CONTROL + "a")
            no_of_rater.send_keys(Keys.DELETE)
            time.sleep(1)
            no_of_rater.send_keys(No_of_rater)
            is_mandatory.click()
            time.sleep(1)
            save.click()
            time.sleep(2)
            rows2 = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div"))))

            if(rows+1 == rows2):
                body.append(
                    f"Both Switches off in Rater Category: Pass    {dt_string}")
                assert True
            else:
                cancel.click()
                time.sleep(1)
                body.append(
                    f"Both Switches off in Rater Category: Fail    {dt_string}")
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
        #     subject = "HRMS-360 Alpha-Testing Login"
        #     message = f"subject:{subject}\n\n{body[0]}\n{body[1]}\n{body[2]}\n{body[3]}\n{body[4]}\n{body[5]}\n"
        #     smtp.sendmail(sender, receiver, message)
        #     print("Email Sent")
        self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(RATERS("test_blankCategory"))
    suite.addTest(RATERS("test_255Category"))
    suite.addTest(RATERS("test_256Category"))
    suite.addTest(RATERS("test_negativeRaters"))
    suite.addTest(RATERS("test_bothSwitchOn"))
    suite.addTest(RATERS("test_bothSwitchOff"))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
    # unittest.main()
