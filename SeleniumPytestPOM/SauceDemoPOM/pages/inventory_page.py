from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    ADD_PRODUCT = "add-to-cart-sauce-labs-onesie"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, self.ADD_PRODUCT))
        ).click()