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

        driver.get("https://trytestingthis.netlify.app/")
        time.sleep(2)

        # browser interactions
        title = driver.title
        print(title)

        url = driver.current_url
        print(url)

        time.sleep(2)

        # navigational commands
        driver.back()
        time.sleep(2)

        driver.forward()
        time.sleep(2)

        driver.refresh()