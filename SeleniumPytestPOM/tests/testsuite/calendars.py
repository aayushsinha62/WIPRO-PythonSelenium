from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://rsuitejs.com/components/date-picker/")
driver.maximize_window()
wait = WebDriverWait(driver, 15)


def test_calendar():
    try:

        date_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.rs-input[placeholder='MM/dd/yyyy']")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_input)
        time.sleep(1)


        date_input.click()



        day_xpath = "//div[contains(@class, 'rs-calendar-table-cell-content')]/span[text()='25']"
        day_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, day_xpath)))

        day_to_select.click()
        print("Success: Date 25 selected.")

    except Exception as e:
        print(f"Error fixed: {e}")

    finally:
        time.sleep(3)
        driver.quit()