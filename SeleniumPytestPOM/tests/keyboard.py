import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Test_Keyboard:

    def test_keyboard(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        time.sleep(2)

        actions = ActionChains(driver)
        email = driver.find_element(By.XPATH, "//input[@name='email']")
        seriesofactions = (
            actions
            .move_to_element(email)
            .key_down(Keys.SHIFT)
            .send_keys("hello")
            .key_up(Keys.SHIFT)
        )
        seriesofactions.perform()

        actions = ActionChains(driver)
        password = driver.find_element(By.XPATH, "//input[@name='pass']")

        seriesofactions = (
            actions
            .click(password)
            .key_down(Keys.SHIFT)
            .send_keys("yes")
        )
        seriesofactions.perform()

        sleep(2)

        driver.close()