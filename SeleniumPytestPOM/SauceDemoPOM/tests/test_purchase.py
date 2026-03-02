import os
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.excel_reader import read_test_data
from utils.logger import get_logger
from utils.screenshot import take_screenshot



PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_PATH = os.path.join(PROJECT_ROOT, "testdata", "testdata.xlsx")


test_data = read_test_data(EXCEL_PATH, "Sheet1")

logger = get_logger()


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("data", test_data)
class TestPurchase:

    def test_end_to_end_purchase(self, data):
        try:
            self.driver.get("https://www.saucedemo.com/")
            logger.info("Opened SauceDemo")

            # login object
            LoginPage(self.driver).login(
                data["username"],
                data["password"]
            )


            if data["expected"] == "failure":
                logger.info("Invalid credentials scenario")
                error = self.driver.find_element(
                    "xpath",
                    "//h3[@data-test='error']"
                )
                assert error.is_displayed()
                return

            logger.info("Login successful")

            # cart, inventory and checkout objects
            InventoryPage(self.driver).add_product()
            logger.info("Product added to cart")

            CartPage(self.driver).go_to_checkout()
            CheckoutPage(self.driver).complete_checkout(
                data["firstname"],
                data["lastname"],
                data["postal"]
            )


            assert "checkout-complete" in self.driver.current_url
            logger.info("Order completed successfully")

        except Exception as e:

            logger.error("Test failed")
            take_screenshot(self.driver, "failure")
            raise e