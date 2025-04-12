from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.cloudgensoft.com")
time.sleep(10)
driver.quit()

