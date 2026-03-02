from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class ManagerPage(BasePage):

    ADD_CUSTOMER_TAB = (By.XPATH, "//button[normalize-space()='Add Customer']")
    OPEN_ACCOUNT_TAB = (By.XPATH, "//button[normalize-space()='Open Account']")
    CUSTOMERS_TAB = (By.XPATH, "//button[normalize-space()='Customers']")

    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    POST_CODE = (By.XPATH, "//input[@placeholder='Post Code']")
    ADD_CUSTOMER_BTN = (By.XPATH, "//button[@type='submit']")

    CUSTOMER_DROPDOWN = (By.ID, "userSelect")
    CURRENCY_DROPDOWN = (By.ID, "currency")
    PROCESS_BTN = (By.XPATH, "//button[normalize-space()='Process']")

    def add_customer(self, fname, lname, postcode):
        self.click(self.ADD_CUSTOMER_TAB)
        self.type(self.FIRST_NAME, fname)
        self.type(self.LAST_NAME, lname)
        self.type(self.POST_CODE, postcode)
        self.click(self.ADD_CUSTOMER_BTN)

    def open_account(self, customer_name, currency):
        self.click(self.OPEN_ACCOUNT_TAB)

        customer_dropdown = self.wait.until(
            lambda d: d.find_element(*self.CUSTOMER_DROPDOWN)
        )
        Select(customer_dropdown).select_by_visible_text(customer_name)

        currency_dropdown = self.wait.until(
            lambda d: d.find_element(*self.CURRENCY_DROPDOWN)
        )
        Select(currency_dropdown).select_by_visible_text(currency)

        self.click(self.PROCESS_BTN)