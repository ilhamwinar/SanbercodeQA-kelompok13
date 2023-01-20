import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from data_input import inputan


class TestLoginRegister(unittest.TestCase): 
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    def test_Login_Positif(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/#") 
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(1)").click()
        time.sleep(3)
        driver.find_element(By.ID,"FirstName").send_keys(inputan.First_name)
        time.sleep(3)
        driver.find_element(By.ID,"Surname").send_keys(inputan.Surname)
        time.sleep(3)
        driver.find_element(By.ID,"E_post").send_keys(inputan.E_post)
        time.sleep(3)
        driver.find_element(By.ID,"Mobile").send_keys(inputan.Mobile)
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys(inputan.Username)
        time.sleep(3)
        driver.find_element(By.ID,"Password").send_keys(inputan.Password)
        time.sleep(3)
        driver.find_element(By.ID,"ConfirmPassword").send_keys(inputan.Password)
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='submit']").click()
        time.sleep(10)

unittest.main()