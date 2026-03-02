import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Test_Keyboard:

    def test_keyboard(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        driver.get("https://www.facebook.com/")
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)

        # Locate fields
        email = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
        password = wait.until(EC.element_to_be_clickable((By.NAME, "pass")))

        # 1️⃣ Type username
        email.click()
        email.send_keys("hello")

        # 2️⃣ Copy username (CTRL + A, CTRL + C)
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL)\
               .send_keys("a")\
               .send_keys("c")\
               .key_up(Keys.CONTROL)\
               .perform()

        # 3️⃣ Paste into password (CTRL + V)
        password.click()
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL)\
               .send_keys("v")\
               .key_up(Keys.CONTROL)\
               .perform()

        # 4️⃣ Click 👁️ Show password icon
        eye_icon = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@aria-label='Show password']//*[name()='svg']")
            )
        )
        eye_icon.click()

        # 5️⃣ Verify password is visible
        assert password.get_attribute("type") == "text"

        sleep(3)
        driver.quit()