from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/radio.html")
radio1=driver.find_element(By.ID, "vfb-7-1")
radio1.click()
checkbox1=driver.find_element(By.ID, "vfb-6-0")
checkbox1.click()
time.sleep(15)
driver.quit()