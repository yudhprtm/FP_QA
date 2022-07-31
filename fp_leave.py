from random import random
from select import select
from tkinter.tix import Select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class admin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def TC_leave(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_Configure").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_leave_leaveTypeList"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.ID,"leaveType_txtLeaveTypeName").send_keys("CAN - Istri Melahirkan")
        time.sleep(2)
        browser.find_element(By.XPATH,'//*[@id="leaveType_excludeIfNoEntitlement"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"saveButton").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"resultTable").text
        
        self.assertIn("US - Istri Melahirkan",response_data)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
