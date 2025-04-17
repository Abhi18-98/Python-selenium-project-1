from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://cloudgensoftech.in/Program6_LoginUsingIDLocator.html")
driver.maximize_window()
driver.find_element(By.ID,"username").send_keys("abhishek")
driver.find_element(By.ID,"password").send_keys("abhishek@123")
driver.find_element(By.ID, "loginForm").submit()
time.sleep(10)
driver.quit()