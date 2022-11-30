from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from datetime import datetime

EMAIL = "meenaz@apsis.com"
PASSWORD = "1234"
TITLE = "Questionnaire 2"
DESCRIPTION = "Automated Testing"
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


class addQuestionnaire(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addQuestionnaire(self):
        driver = self.driver
        try:
            driver.get("http://192.168.10.60:3000/sign-in")

        except Exception:
            print(Exception)
        else:
            driver.maximize_window()
            time.sleep(2)
            username = driver.find_element(
                By.NAME, "email")
            password = driver.find_element(
                By.NAME, "password")
            show_password = driver.find_element(By.CSS_SELECTOR, "svg")
            sign_in = driver.find_element(
                By.XPATH, "//button[normalize-space()='Sign in']")
            username.send_keys(EMAIL)
            password.send_keys(PASSWORD)
            time.sleep(1)
            show_password.click()
            time.sleep(1)
            sign_in.click()
            time.sleep(3)

            cur_url = driver.current_url
            expected_url = "http://192.168.10.60:3000/"
            time.sleep(2)

            try:
                self.assertEqual(expected_url, cur_url,
                                 "Result is not matched with expected")

            except Exception:
                print("something went wrong in matching urls")

            else:
                time.sleep(2)
                questionnaire_tab = driver.find_element(
                    By.XPATH, "//*[@id='__next']/div[1]/nav/div/div/div/ul/li[3]")
                questionnaire_tab.click()
                time.sleep(1)
                cur_url = driver.current_url
                expected_url = "http://192.168.10.60:3000/questions-bank"
                try:
                    self.assertEqual(expected_url, cur_url,
                                     "link doesn't match")
                except Exception:
                    print("error in matching links")

                else:
                    add_questionnaire = driver.find_element(
                        By.CSS_SELECTOR, ".cursor-pointer.p-3.rounded-lg.flex.items-center.justify-center.font-light.text-xl.mr-4.w-80.MuiBox-root.css-1llh69y")
                    add_questionnaire.click()
                    time.sleep(2)
                    cur_url = driver.current_url
                    expected_url = "http://192.168.10.60:3000/questions-bank/add"

                    try:
                        self.assertEqual(
                            expected_url, cur_url, "Url not macthed")
                    except:
                        print("error in matching urls")

                    else:
                        time.sleep(2)
                        title = driver.find_element(By.NAME, "title")
                        description = driver.find_element(
                            By.NAME, "description")
                        save = driver.find_element(
                            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div/div[5]/button")
                        title.send_keys(TITLE)
                        description.send_keys(DESCRIPTION)
                        time.sleep(2)
                        save.click()
                        time.sleep(2)
                        check1 = driver.find_element(
                            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/input")
                        check2 = driver.find_element(
                            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div[1]/span/input")
                        check1.click()
                        check2.click()
                        time.sleep(2)
                        next = driver.find_element(
                            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div[1]/div[2]/button[2]")
                        next.click()
                        time.sleep(2)
                        add_question1 = driver.find_element(
                            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[5]/div/button[1]")
                        add_question1.click()
                        time.sleep(2)
                        checkbox1 = driver.find_element(
                            By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]/label/span[1]/input")
                        checkbox1.click()
                        time.sleep(2)
                        save = driver.find_element(
                            By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/div/div[3]/button[2]")
                        save.click()
                        time.sleep(2)
                        add_question2 = driver.find_element(
                            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[5]/div/button[1]")
                        add_question2.click()
                        time.sleep(2)
                        checkbox2 = driver.find_element(
                            By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]/label/span[1]/input")
                        checkbox2.click()
                        time.sleep(2)
                        save2 = driver.find_element(
                            By.XPATH, "//*[@id='main']/div[2]/div[3]/div/div/div/div/div/div[3]/button[2]")
                        save2.click()
                        time.sleep(2)
                        create = driver.find_element(
                            By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/form/div/div/div[2]/div/div/div[1]/div[2]/button[2]")
                        create.click()
                        time.sleep(2)

                        cur_url = driver.current_url
                        expected_url = "http://192.168.10.60:3000/questions-bank/my"

                        try:
                            self.assertEqual(expected_url, cur_url,
                                             "Test Case Failed")
                            file = open("Manager_Report.txt", "a")
                            file.write(
                                "\nAdd Questionnaire: Pass\t Date:")
                            file.write(dt_string)

                        except:
                            file = open("Manager_Report.txt", "a")
                            file.write(
                                "\nAdd Questionnaire: Fail\t Date:")
                            file.write(dt_string)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
