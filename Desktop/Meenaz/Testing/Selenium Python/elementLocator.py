from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class DemoFindElementById():
    def locate_by_id(self):
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID, "login-input").send_keys("test@test.com")
        time.sleep(4)


class DemoFindElementByName():
    def locate_by_name(self):
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.NAME, "login-input").send_keys("test@test.com")
        time.sleep(4)


class DemoFindElementByXPath():
    def locate_by_xpath(self):
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(
            By.XPATH, "//input[@id='login-input']").send_keys("test@test.com")
        time.sleep(4)


class DemoFindElementBycssSelector():
    def locate_by_css_selector(self):
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(
            By.CSS_SELECTOR, "#login-input").send_keys("test@test.com")
        time.sleep(4)


# findbyid = DemoFindElementById()
# findbyid.locate_by_id()

# findbyxpath = DemoFindElementByXPath()
# findbyxpath.locate_by_xpath()

findbycss = DemoFindElementBycssSelector()
findbycss.locate_by_css_selector()
