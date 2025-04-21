from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://cloudgensoftech.in/Program10_MultiWindowHandlingScenario.html")
driver.maximize_window()
parent_window=driver.current_window_handle
print("Parent Window Handle", parent_window)
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)
all_windows=driver.window_handles
print("All Window Handles", all_windows)
for handle in all_windows:
    if handle!=parent_window:
        driver.switch_to.window(handle)
        print("Switch to Child Window", handle)
        break
time.sleep(10)
driver.close()
print("Child Window Closed")   
driver.switch_to.window(parent_window)
print("Switched Back to Parent Window", parent_window)
time.sleep(10)
driver.quit()

