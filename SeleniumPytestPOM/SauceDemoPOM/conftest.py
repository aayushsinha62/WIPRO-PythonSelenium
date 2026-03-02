# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
#
# @pytest.fixture(scope="class")
# def driver(request):
#     options = Options()
#     options.add_argument("--incognito")
#     options.add_argument("--start-maximized")
#
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=options
#     )
#
#     request.cls.driver = driver
#     yield
#     driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def driver(request):
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )

    request.cls.driver = driver
    yield
    driver.quit()