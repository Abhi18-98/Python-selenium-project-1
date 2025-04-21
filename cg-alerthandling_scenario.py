from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://cloudgensoftech.in/Program9_AlertHandlingScenario.html")
driver.maximize_window()
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)
alert=driver.switch_to.alert
alert.accept
time.sleep(10)
driver.quit()

