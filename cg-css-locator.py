from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://cloudgensoftech.in/Program8_LoginUsingCSSSelector.html")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#cssEmail").send_keys("abhi@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#cssPass").send_keys("abhi123")
driver.find_element(By.CSS_SELECTOR,"button").click()
time.sleep(10)
driver.quit()
























