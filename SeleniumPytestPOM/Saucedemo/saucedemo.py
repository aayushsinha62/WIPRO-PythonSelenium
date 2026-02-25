from asyncio import timeout
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# ==============================
# CONSTANTS / TEST DATA
# ==============================

URL = "https://www.saucedemo.com/"

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

FIRST_NAME = "Aayush"
LAST_NAME = "Sinha"
POSTAL_CODE = "751024"

PRODUCT_ID = "add-to-cart-sauce-labs-onesie"


# ==============================
# FIXTURE: Browser Setup
# ==============================

@pytest.fixture(scope="class")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    yield driver
    driver.quit()


# ==============================
# REUSABLE ACTION FUNCTIONS
# ==============================

def login(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(URL)

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))) \
        .send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url


def add_item_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.element_to_be_clickable((By.ID, PRODUCT_ID))
    ).click()

    badge = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1"


def checkout(driver):
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))) \
        .send_keys(FIRST_NAME)
    driver.find_element(By.ID, "last-name").send_keys(LAST_NAME)
    driver.find_element(By.ID, "postal-code").send_keys(POSTAL_CODE)

    driver.find_element(By.ID, "continue").click()
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()


def verify_order_success(driver):
    wait = WebDriverWait(driver, 10)

    thank_you = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[normalize-space()='Thank you for your order!']")
        )
    )

    assert thank_you.is_displayed()


# ==============================
# TEST CASES
# ==============================

class TestSauceDemoPurchase:

    def test_login(self, driver):
        login(driver)

    def test_add_item_to_cart(self, driver):
        add_item_to_cart(driver)

    def test_checkout(self, driver):
        checkout(driver)

    def test_verify_order_success(self, driver):
        verify_order_success(driver)