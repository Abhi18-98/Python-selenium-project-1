from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

driver.get("https://cloudgensoftech.in/click_action.html")
driver.maximize_window()

click_action=driver.find_element(By.ID, "clickButton")
click_action.click()
time.sleep(10)

status_text=driver.find_element(By.ID, "statusText").text
print("status after button click",status_text)

click_link=driver.find_element(By.ID, "clickLink")
click_link.click()
time.sleep(10)

status_text=driver.find_element(By.ID, "statusText").text
print("status after  click",status_text)

description=driver.find_element(By.ID, "descriptionText").text
print("status after  click",description)
time.sleep(10)

driver.quit()