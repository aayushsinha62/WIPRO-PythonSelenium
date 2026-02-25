import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_demowebshop_e2e():

    # URL variable
    url = "https://demowebshop.tricentis.com/login"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        #Open Website
        driver.get(url)
        time.sleep(2)

        #Login
        driver.find_element(By.ID, "Email").send_keys("aayushsinha01@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("test@123")
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        time.sleep(3)

        print("Login Successful")

        #Search Product
        driver.find_element(By.ID, "small-searchterms").send_keys("Laptop")
        driver.find_element(By.XPATH, "//input[@value='Search']").click()
        time.sleep(2)

        #Add Product to Cart
        driver.find_element(By.XPATH, "//input[@value='Add to cart']").click()
        time.sleep(2)

        print("Product Added to Cart")

        #Go to Shopping Cart
        driver.find_element(By.XPATH, "//span[text()='Shopping cart']").click()
        time.sleep(2)

        #Accept Terms of Service
        driver.find_element(By.ID, "termsofservice").click()
        time.sleep(1)

        #Click Checkout
        driver.find_element(By.ID, "checkout").click()
        time.sleep(3)

        #Confirm Order (if already has address saved)
        driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@value='Confirm']").click()
        time.sleep(3)

        #Validate Order Success
        success_text = driver.find_element(By.CLASS_NAME, "title").text
        assert "Your order has been successfully processed!" in success_text

        print("Order Placed Successfully")

    except Exception as e:
        print("Test Failed Due To:", e)

    finally:
        time.sleep(3)
        driver.quit()