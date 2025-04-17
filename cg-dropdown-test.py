from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()

driver.get("https://cloudgensoftech.in/Program4_DropdownSelection.html")
driver.maximize_window()

drop_down=Select(driver.find_element(By.NAME,"country"))
drop_down.select_by_visible_text("India")
time.sleep(10)
drop_down.select_by_index(2)
time.sleep(10)
drop_down.select_by_value("india")
time.sleep(10)
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(10)
driver.quit()

