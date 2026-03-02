import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_radiobutton:
    def test_radiobutton(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://testautomationpractice.blogspot.com/')

        time.sleep(4)

        #click on checkbox one by one
        checkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        count=  len(checkbox_list)
        print(count)

        #iterate the list
        limit=7
        for i in checkbox_list[:limit]:
            time.sleep(2)
            i.click()

        driver.close()


