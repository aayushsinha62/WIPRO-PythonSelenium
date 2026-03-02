from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class AccountPage(BasePage):


    DEPOSIT_TAB = (By.XPATH, "//button[normalize-space()='Deposit']")
    WITHDRAW_TAB = (By.XPATH, "//button[contains(text(),'Withdraw')]")


    DEPOSIT_AMOUNT_INPUT = (
        By.XPATH, "//form[contains(@ng-submit,'deposit')]//input[@placeholder='amount']"
    )
    WITHDRAW_AMOUNT_INPUT = (
        By.XPATH, "//form[contains(@ng-submit,'withdraw')]//input[@placeholder='amount']"
    )

    DEPOSIT_SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")
    WITHDRAW_SUBMIT_BTN = (By.XPATH, "//button[normalize-space()='Withdraw']")


    MESSAGE = (By.XPATH, "//span[@class='error ng-binding']")
    BALANCE = (By.XPATH, "//strong[2]")

    def deposit_amount(self, amount):
        self.click(self.DEPOSIT_TAB)

        amt = self.wait.until(
            EC.element_to_be_clickable(self.DEPOSIT_AMOUNT_INPUT)
        )
        amt.clear()
        amt.send_keys(str(amount))

        self.click(self.DEPOSIT_SUBMIT_BTN)

        return self.wait.until(
            EC.visibility_of_element_located(self.MESSAGE)
        ).text

    def withdraw_amount(self, amount):
        self.click(self.WITHDRAW_TAB)

        amt = self.wait.until(
            EC.element_to_be_clickable(self.WITHDRAW_AMOUNT_INPUT)
        )
        amt.clear()
        amt.send_keys(str(amount))

        self.click(self.WITHDRAW_SUBMIT_BTN)

        return self.wait.until(
            EC.visibility_of_element_located(self.MESSAGE)
        ).text

    def get_balance(self):
        return int(self.get_text(self.BALANCE))