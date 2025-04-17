from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://cloudgensoftech.in/Program7_LoginUsingXPathLocator.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='x_user']").send_keys("abhishek")
driver.find_element(By.XPATH,"//input[@id='x_pass']").send_keys("abhishek@123")
driver.find_element(By.XPATH, "//button[@type='button']").submit()
time.sleep(10)
driver.quit()