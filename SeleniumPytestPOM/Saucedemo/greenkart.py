from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


# ==============================
# CONSTANTS / TEST DATA
# ==============================

URL = "https://rahulshettyacademy.com/seleniumPractise/#/"



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


def add_item_to_cart(driver):
    driver.get(URL)

    wait = WebDriverWait(driver,10 )

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//button[@type='button'][normalize-space()='ADD TO CART'])[12]")
        )
    ).click()

    badge_text = driver.execute_script(
        "return document.querySelector('strong').innerText;"
    )

    assert badge_text.strip() == "1"

    sleep(5)


def checkout(driver):
    wait = WebDriverWait(driver, 10)

    cart = driver.find_element(By.XPATH, "//img[@alt='Cart']")
    driver.execute_script("arguments[0].click();", cart)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']"))).click()


def placeorder(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Place Order']"))).click()

def selectcountry(driver):
    wait = WebDriverWait(driver, 10)

    dropdown_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='wrapperTwo']//div//select"))
    )

    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("India")

    selected_option = dropdown.first_selected_option.text
    assert selected_option == "India"

def checkbox(driver):
    wait = WebDriverWait(driver, 10)

    checkboxx = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']"))
    )

    if not checkboxx.is_selected():
        checkboxx.click()

    assert checkboxx.is_selected()


def proceed(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Proceed']"))).click()

def verify_order_success(driver):
    wait = WebDriverWait(driver, 10)

    thank_you = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(),'Thank you, your order has been placed successfully')]")
        )
    )



    assert thank_you.is_displayed()


# ==============================
# TEST CASES
# ==============================
class Test_GreenKart:
    def test_add_item_to_cart(self,driver):
        add_item_to_cart(driver)


    def test_placeorder(self,driver):
        placeorder(driver)

    def test_select_country(self, driver):
        selectcountry(driver)


    def test_checkbox(self,driver):
        checkbox(driver)


    def test_proceed(self,driver):
        proceed(driver)


    def test_verify_order_success(self,driver):
        verify_order_success(driver)
