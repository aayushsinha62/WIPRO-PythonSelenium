from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    CUSTOMER_LOGIN = (By.XPATH, "//button[normalize-space()='Customer Login']")
    MANAGER_LOGIN = (By.XPATH, "//button[normalize-space()='Bank Manager Login']")
    HOME_BTN = (By.XPATH, "//button[normalize-space()='Home']")

    def click_customer_login(self):
        self.click(self.CUSTOMER_LOGIN)

    def click_manager_login(self):
        self.click(self.MANAGER_LOGIN)

    def go_home(self):
        self.click(self.HOME_BTN)