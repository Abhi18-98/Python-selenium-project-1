import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time
class TestCloudGenSoftechRadioButton(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://cloudgensoftech.in/radio_test.html")
        self.driver.maximize_window()
    def test_select_first_radio_button(self):
        radio_button=WebDriverWait(self.driver, 10). until(EC.element_to_be_clickable((By.ID,"radio1")))
        radio_button.click()
        self.assertTrue(radio_button.is_selected(), "Radio Button 1 should be selected")

    def test_select_first_radio_button(self):
        radio_button=WebDriverWait(self.driver, 10). until(EC.element_to_be_clickable((By.ID,"radio2")))
        radio_button.click()
        self.assertTrue(radio_button.is_selected(), "Radio Button 2 should be selected")
        
     
    def test_select_first_radio_button(self):
        radio_button=WebDriverWait(self.driver, 10). until(EC.element_to_be_clickable((By.ID,"radio3")))
        radio_button.click()
        self.assertTrue(radio_button.is_selected(), "Radio Button 3 should be selected")

    def tearDown(self):
        self.driver.quit()
if __name__== '__main__':
    unittest.main()            
    
   






       