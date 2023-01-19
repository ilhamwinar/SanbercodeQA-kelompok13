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
        # time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(2) > a").click()
        # time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"body > div > div:nth-child(2) > p > button").click()
        time.sleep(3)
        response_massage= driver.find_element(By.CSS_SELECTOR,"#collapse1").text
        print(response_massage)
        if "import" in response_massage:
            print("DATA SOLUTION 1 OK")
        else:
            print('DATA SOLUTION 1 NOK')

        driver.find_element(By.CSS_SELECTOR,"body > div > div:nth-child(3) > p > button").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 1200)") 
        response_massage2= driver.find_element(By.CSS_SELECTOR,"#collapse2").text
        print(response_massage2)
        if "import" in response_massage2:
            print("DATA SOLUTION 2 OK")
        else:
            print('DATA SOLUTION 2 NOK')
        driver.find_element(By.CSS_SELECTOR,"body > div > div:nth-child(4) > p > button").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 1500)") 
        response_massage3= driver.find_element(By.CSS_SELECTOR,"#collapse3").text
        print(response_massage3)
        if "import" in response_massage3:
            print("DATA SOLUTION 3 OK")
        else:
            print('DATA SOLUTION 3 NOK')
        driver.find_element(By.CSS_SELECTOR,"body > div > div:nth-child(5) > p > button").click()
        driver.execute_script("window.scrollTo(0, 1500)")
        time.sleep(3)
        response_massage4= driver.find_element(By.CSS_SELECTOR,"#collapse4").text
        print(response_massage4)
        if "import" in response_massage4:
            print("DATA SOLUTION 4 OK")
        else:
            print('DATA SOLUTION 4 NOK')
            
unittest.main()