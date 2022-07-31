import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TC_search(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_search_employee(self):
        # steps
        browser = self.browser #buka web browse
        browser.get("https://opensource-demo.orangehrmlive.com/ ") #buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input").send_keys("Admin") #isi username
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("admin123") #isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik tombol login
        time.sleep(3)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() #go to menu pim
        time.sleep(1)
        browser.find_element(By.ID,"empsearch_employee_name_empName").send_keys("Admin A") #isi name
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click() #cari
        time.sleep(1)
        
    def TC_PIM_delete(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_Configuration").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_pim_listCustomFields"]').click()
        time.sleep(1)
        fieldDel = browser.find_element(By.XPATH,'//*[@id="customFieldList"]/tbody/tr[1]/td[2]').text
        browser.find_element(By.XPATH,'//*[@id="customFieldList"]/tbody/tr[1]/td[1]/input').click()
        time.sleep(1)
        browser.find_element(By.ID,"buttonRemove").click()
        time.sleep(1)
        browser.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"customFieldList").text

        self.assertNotIn(fieldDel,response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__":
    unittest.main()