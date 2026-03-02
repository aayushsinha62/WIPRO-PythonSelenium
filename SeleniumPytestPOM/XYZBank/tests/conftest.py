import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import get_logger
from utils.screenshot import take_screenshot

logger = get_logger()


@pytest.fixture
def driver(request):
    logger.info("Launching browser")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(
        "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    )

    yield driver


    if request.node.rep_call.failed:
        logger.error(f"Test failed: {request.node.name}")
        take_screenshot(driver, request.node.name)

    logger.info("Closing browser")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)