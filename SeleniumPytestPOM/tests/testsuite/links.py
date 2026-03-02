import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Test_Upload:

    def test_up(self):

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        links = driver.find_elements(By.TAG_NAME, "a")
        count = len(links)
        print(count)

        for link in links:
            print(link.text)

        time.sleep(2)
        driver.close()