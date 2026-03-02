from pages.login_page import LoginPage
from pages.manager_page import ManagerPage
from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()

def test_manager_add_customer_and_open_account(driver):
    login = LoginPage(driver)
    manager = ManagerPage(driver)
    wait = WebDriverWait(driver, 5)

    login.click_manager_login()
    logger.info("Manager login clicked")

    manager.add_customer("Aayush", "Sinha", "110011")

    alert = wait.until(EC.alert_is_present())
    logger.info(alert.text)
    alert.accept()

    manager.open_account("Aayush Sinha", "Dollar")

    alert = wait.until(EC.alert_is_present())
    logger.info(alert.text)
    alert.accept()