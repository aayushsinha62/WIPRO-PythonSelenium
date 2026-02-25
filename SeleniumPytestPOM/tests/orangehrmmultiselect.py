import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_orangeHRM:
    def test_orangeHRM(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        time.sleep(4)

        # enter username
        name = driver.find_element(By.NAME, "username")
        name.send_keys("Admin")

        # enter password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")

        time.sleep(4)

        # click on login button
        Login = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        Login.click()

        time.sleep(10)


        # click on PIM link
        pim = driver.find_element(By.LINK_TEXT, "PIM")
        pim.click()

        time.sleep(10)

        # click on checkbox one by one
        checkbox_list = driver.find_elements(By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])")
        count = len(checkbox_list)
        print(count)

        # iterate the list
        start=1
        for i in checkbox_list[start:]:
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});",i)
            time.sleep(2)
            i.click()

        driver.close()

