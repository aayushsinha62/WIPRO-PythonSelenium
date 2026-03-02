from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
from pages.account_page import AccountPage
from utils.excel_reader import ExcelReader
from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()
excel = ExcelReader("data/testdata.xlsx")

def test_customer_transaction_flow(driver):
    login = LoginPage(driver)
    customer = CustomerPage(driver)
    account = AccountPage(driver)
    wait = WebDriverWait(driver, 5)

    customer_data = excel.get_data("CustomerLogin")
    transaction_data = excel.get_data("Transaction")

    for user, txn in zip(customer_data, transaction_data):
        logger.info(f"Starting test for {user['CustomerName']}")


        login.click_customer_login()


        wait.until(EC.visibility_of_element_located(customer.USER_SELECT))
        customer.login_customer(user["CustomerName"])

        assert customer.is_logged_in()
        logger.info("Customer logged in successfully")

        before_balance = account.get_balance()


        deposit_msg = account.deposit_amount(txn["Deposit"])
        logger.info(deposit_msg)
        assert "deposit" in deposit_msg.lower()


        withdraw_msg = account.withdraw_amount(txn["Withdraw"])
        logger.info(withdraw_msg)

        after_balance = account.get_balance()
        balance_change = after_balance - before_balance

        if "transaction" in withdraw_msg.lower():
            expected_change = txn["Deposit"] - txn["Withdraw"]
        else:
            expected_change = txn["Deposit"]

        assert balance_change == expected_change
        logger.info("Balance validated successfully")


        customer.click(customer.LOGOUT_BTN)
        wait.until(EC.visibility_of_element_located(login.HOME_BTN))
        login.go_home()
