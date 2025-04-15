from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
dropdown=Select(driver.find_element(By.ID,"Skills"))
dropdown.select_by_visible_text("C")
print("dropdownvalue Clanguage selected")
time.sleep(10)
driver.quit()

