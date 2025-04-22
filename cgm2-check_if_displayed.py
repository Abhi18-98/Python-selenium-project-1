from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://cloudgensoftech.in/check_if_displayed.html")
driver.maximize_window()
time.sleep(4)
check_element=driver.find_element(By.ID, "toggleBtn")
time.sleep(3)
assert check_element.is_displayed(By.ID, "checkVisibilityBtn")
time.sleep(10)
driver.quit()