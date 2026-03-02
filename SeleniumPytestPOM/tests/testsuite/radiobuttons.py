import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_Radio:
    def test_radio(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://rahulshettyacademy.com/AutomationPractice/')

        time.sleep(4)

        # click on radio button
        Radio = driver.find_element(By.XPATH, "//input[@value='radio2']")
        Radio.click()

        #click on checkbox
        Checkbox = driver.find_element(By.XPATH, "// input[ @ id = 'checkBoxOption2']")
        Checkbox.click()



