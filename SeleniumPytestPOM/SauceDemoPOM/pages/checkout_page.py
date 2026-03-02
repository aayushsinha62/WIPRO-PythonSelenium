from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def complete_checkout(self, first, last, postal):
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "finish").click()