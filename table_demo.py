from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/table.html")
rows=driver.find_elements(By.TAG_NAME,"tr")
print ("Total rows:", len(rows))
for row in rows:
    cells=row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text, end=" | ")
    print()  
time.sleep(10)     
driver.quit()



