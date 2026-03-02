from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CustomerPage(BasePage):

    USER_SELECT = (By.ID, "userSelect")
    LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Login']")
    LOGOUT_BTN = (By.XPATH, "//button[normalize-space()='Logout']")
    WELCOME_TEXT = (By.XPATH, "//strong[contains(text(),'Welcome')]")

    def login_customer(self, customer_name):

        customer_dropdown = self.wait.until(
            EC.presence_of_element_located(self.USER_SELECT)
        )

        Select(customer_dropdown).select_by_visible_text(customer_name)
        self.click(self.LOGIN_BTN)

    def is_logged_in(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGOUT_BTN)
        ).is_displayed()