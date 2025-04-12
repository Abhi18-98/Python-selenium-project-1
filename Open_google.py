from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://cloudgensoft.com")
input("press enter to close webpage")
driver.quit()
