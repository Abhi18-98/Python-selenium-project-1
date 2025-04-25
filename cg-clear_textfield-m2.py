from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://cloudgensoftech.in/clear_text_field.html")
driver.maximize_window()
time.sleep(2)
input_field=driver.find_element(By.ID,"inputField")
input_field.send_keys("this is automation test script")
print("text entered into output field")
time.sleep(5)
clear_button=driver.find_element(By.ID,"clearBtn")
clear_button.click()
time.sleep(5)
cleared_text=input_field.get_attribute("value")
if cleared_text == "":
    print("Test Field has been completely cleared")
else:
    print("Test field has not not cleared")
time.sleep(10)
driver.quit()    