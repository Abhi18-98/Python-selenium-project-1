from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC 
driver=webdriver.Chrome()
driver.get("https://cloudgensoftech.in/check_if_displayed.html")
driver.maximize_window()
time.sleep(10)
try:
	wait=WebDriverWait(driver, 10)
	element=wait.until(EC.presence_of_element_located((By.ID, "toggleBtn")))
	if element.is_displayed():
		print("The Element Is Visible on The Page")
	else:
		print("The Element Is Present But Not Visible on the Page")
except Expection as e:
	print(f"test failed: {e}")
finally:
	driver.quit()	


			
