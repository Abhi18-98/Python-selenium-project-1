from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://cloudgensoftech.in/Program10_MultiWindowHandlingScenario.html")
driver.maximize_window()
main_window=driver.current_window_handle
driver.find_element(By.LINK_TEXT, "Open New Tab").click()
time.sleep(10)
all_windows=driver.window_handles
for handle in all_windows:
    if handle != main_window:
        driver._switch_to.window(handle)
        break
time.sleep(10)
driver.close()
driver.switch_to.window(main_window)
time.sleep(5)
driver.quit()    