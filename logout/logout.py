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


    def test_Login_TC051_Positif(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/#") 
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(2)").click()
        # time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("kelompok_13")
        # time.sleep(3)
        driver.find_element(By.ID,"Password").send_keys("kelompok_13")
        # time.sleep(3)
        driver.find_element(By.NAME,"login").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(2)").click()
        response_massage= driver.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[1]/td[2]").text
        # print(response_massage)
        time.sleep(3)
        if "LOGIN" in response_massage:
            print("BERHASIL LOGOUT")
        else:
            print('GAGAL LOGOUT')
            
unittest.main()