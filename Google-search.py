from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.google.com")
print ("title", driver.title)
search_box=driver.find_element(By.NAME, "q")
search_box.send_keys("selenium with python")
search_box.submit()
time.sleep(15)
results=driver.find_elements(By.TAG_NAME,"h3")
for result in results[:5]:
    print("Result",result.text)

driver.quit()    