#create a fixture for invoke chrome and close the chrome browser

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    service=Service(ChromeDriverManager().install())
    #driver instance is created to use webdriver globally
    #       in the test script
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https:opensource-demo.orangehrmLive.com/")
    #driver set locally is passed to request at class level
    request.cls.driver=driver
    yield #think like it says ok pytest i am done setting up like opening browser now run testcases and after that come to me
                #and i will perform driver quit for browser
    driver.quit()

