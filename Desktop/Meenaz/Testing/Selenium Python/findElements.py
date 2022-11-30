from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class DemoFindElementByTag():
    def locate_by_tag(self):
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com")
        list = driver.find_elements(By.TAG_NAME, "a")
        print(len(list))
        for i in list:
            print(i.text)
        time.sleep(2)


findbycss = DemoFindElementByTag()
findbycss.locate_by_tag()
