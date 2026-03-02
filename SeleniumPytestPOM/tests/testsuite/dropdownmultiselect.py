import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_dropdown():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://trytestingthis.netlify.app/")

    time.sleep(3)

    # -------- Single Select Dropdown --------
    single_dropdown = driver.find_element(By.ID, "option")
    sel_single = Select(single_dropdown)

    sel_single.select_by_visible_text("Option 2")
    time.sleep(2)

    # Print selected option (single select)
    print("Single Select Dropdown → Selected Option:")
    for option in sel_single.options:
        if option.is_selected():
            print(f" - {option.text}")

    # -------- Multi Select Dropdown --------
    multi_dropdown = driver.find_element(By.ID, "owc")
    sel_multi = Select(multi_dropdown)

    # Select multiple options
    sel_multi.select_by_visible_text("Option 1")
    sel_multi.select_by_visible_text("Option 2")
    sel_multi.select_by_visible_text("Option 3")

    time.sleep(2)

    # Print selected options
    print("Multi Select Dropdown → Selected Options:")
    for option in sel_multi.options:
        if option.is_selected():
            print(f" - {option.text}")

    # -------- Deselect ALL at once --------
    sel_multi.deselect_all()
    time.sleep(2)

    # Print after deselect all
    print("Multi Select Dropdown → After Deselect All:")
    selected = [opt.text for opt in sel_multi.options if opt.is_selected()]
    if not selected:
        print(" - No options selected")

    driver.quit()