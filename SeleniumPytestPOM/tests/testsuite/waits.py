

from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



class Test_frame:

    def test_frame(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.get("https://www.facebook.com/")
        driver.maximize_window()

        # This is a global setting that applies to every element location call for the entire session
        driver.implicitly_wait(2)

        # explicit wait
        radio_btn = driver.find_element(By.XPATH, "(//input[@value='radio2'])[1]")
        wait = WebDriverWait(driver, timeout=2)
        wait.until(lambda _: radio_btn.is_displayed())

        # custom wait or fluent wait
        errors = (NoSuchElementException, ElementNotInteractableException)
        wait = WebDriverWait(
            driver,
            timeout=2,
            poll_frequency=2,
            ignored_exceptions=errors
        )
        wait.until(lambda _: radio_btn.send_keys("Displayed") or True)

        driver.close()