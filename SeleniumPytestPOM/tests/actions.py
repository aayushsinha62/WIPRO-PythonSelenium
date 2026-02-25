import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Actions:

    def test_actions(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.maximize_window()

        driver.get("https://www.amazon.in/")
        time.sleep(4)

        actions=ActionChains(driver)
        bestsellers=driver.find_element(By.XPATH,"//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")

        #double click using actions class
        actions.double_click(bestsellers).perform()
        time.sleep(2)
        driver.back()
        time.sleep(2)

        mobiles = driver.find_element(
            By.XPATH, "//a[normalize-space()='Mobiles']"
        )

        # right click
        actions.context_click(mobiles).perform()
        time.sleep(2)

        time.sleep(2)

        # move to element
        primes = driver.find_element(By.XPATH, "//span[normalize-space()='Prime']")
        actions.move_to_element(primes).perform()

        time.sleep(2)


        fresh = driver.find_element(By.XPATH, "//span[normalize-space()='Fresh']")
        actions.move_to_element(fresh).perform()

        time.sleep(2)

        driver.close()


