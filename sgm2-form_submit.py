from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://cloudgensoftech.in/submit_form.html")
driver.maximize_window()
time.sleep(3)
form_submit=driver.find_element(By.ID,"name")
time.sleep(2)
form_submit.send_keys("Abhishek")
time.sleep(2)
form_submit=driver.find_element(By.ID,"email")
time.sleep(2)
form_submit.send_keys("abhi.g6666@gmail.com")
time.sleep(2)
form_submit=driver.find_element(By.ID,"message")
form_submit.send_keys("Login successful or failed")
time.sleep(2)
form_submit=driver.find_element(By.ID,"submitBtn").click()
driver.quit()

