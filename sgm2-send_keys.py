from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://cloudgensoftech.in/send_keys.html")
driver.maximize_window()
time.sleep(5)
input_element=driver.find_element(By.ID, "inputField")
time.sleep(5)
input_element.send_keys("selenium docs")
time.sleep(2)
input_element.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()