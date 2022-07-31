import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Testlogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") #buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input").send_keys("Admin") #isi username
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("admin123") #isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik tombol login
        time.sleep(3)

    def test_a_failed_login_when_wrong_password(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") #buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input").send_keys("Admin") #isi username
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("Admin123") #isi wrong password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik tombol login
        time.sleep(3)

    def test_a_failed_login_when_empty_password_and_username(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/ ") #buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input").send_keys("") #isi kosong username
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("") #isi kosong password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # lik tombol login
        time.sleep(3)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__":
    unittest.main()