import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_login:
    def test_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://www.saucedemo.com/')

        time.sleep(4)

        # enter username
        name = driver.find_element(By.NAME, "user-name")
        name.send_keys("standard_user")

        # enter password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")

        time.sleep(4)

        # click on login button
        Login = driver.find_element(By.XPATH, "//input[@id='login-button']")
        Login.click()

        # assert "OrangeHRM" in driver.title