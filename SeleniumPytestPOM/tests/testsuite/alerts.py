
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_dropdown():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    time.sleep(3)

    # simple alert with ok button only
    # switch the control to alert
    simplealt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
    simplealt.click()

    alt = driver.switch_to.alert
    alt.accept()  # click on accept button

    time.sleep(5)


    # confirmation alerts
    # switch the control to alert
    confalt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
    confalt.click()

    alt = driver.switch_to.alert
    alt.dismiss()  # click on cancel button

    time.sleep(5)


    # prompt alerts
    promptalt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
    promptalt.click()

    alt = driver.switch_to.alert
    alerttext = alt.text
    print(alerttext)

    alt.send_keys("test hello")
    alt.accept()
    time.sleep(2)

    driver.close()