from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://cloudgensoftech.in/Program5_CheckboxValidation.html")
driver.maximize_window()
check_box=driver.find_elements(By.NAME, "interest")
for checkbox in check_box:
    if not checkbox.is_selected():
        checkbox.click()
    assert checkbox.is_selected(), "checkbox should be selected"
driver.find_element(By.TAG_NAME, "button").click()   

time.sleep(10)
driver.quit()