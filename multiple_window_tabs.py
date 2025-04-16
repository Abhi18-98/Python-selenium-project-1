from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://ditvimilletfoods.com/index.html")
driver.find_element(By.LINK_TEXT, "Our Menu").click()
windows=driver.window_handles
print("Windows List:",windows)
driver.switch_to.window(windows[1])
print("New Window Title:", driver.title)
driver.close()
driver.switch_to.window(windows[0])
print("Parent Window Title", driver.title)
time.sleep(10)
driver.quit()
