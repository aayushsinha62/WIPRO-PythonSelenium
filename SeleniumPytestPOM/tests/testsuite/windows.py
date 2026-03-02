
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_dropdown():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    time.sleep(2)

    driver.implicitly_wait(10)

    clickhere = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
    clickhere.click()

    # fetch window handles of both tabs
    windows = driver.window_handles
    print(windows)

    # move the control to the child window
    driver.switch_to.window(windows[1])

    texts = driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]")
    print(texts.text)

    driver.close()

    # get back to parent window
    driver.switch_to.window(windows[0])
    assert clickhere.is_displayed()

    driver.close()