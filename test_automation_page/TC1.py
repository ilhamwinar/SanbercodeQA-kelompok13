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
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("kelompok_13")
        time.sleep(3)
        driver.find_element(By.ID,"Password").send_keys("kelompok_13")
        time.sleep(3)
        driver.find_element(By.NAME,"login").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(3) > a").click()
        time.sleep(4)
        driver.find_element(By.ID,"name").send_keys(inputan.Name)
        time.sleep(2)
        driver.find_element(By.ID,"phone").send_keys(inputan.Mobile_number)
        time.sleep(2)
        driver.find_element(By.ID,"email").send_keys(inputan.Email_address)
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys(inputan.Password)
        time.sleep(2)
        driver.find_element(By.ID,"address").send_keys(inputan.Address)
        time.sleep(2)
        driver.find_element(By.NAME,"submit").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(3) > a").click()
        time.sleep(4)
        driver.find_element(By.ID,"female").click()
        time.sleep(5)
        driver.find_element(By.ID,"male").click()
        time.sleep(5)
        driver.find_element(By.ID,"monday").click()
        time.sleep(5)
        driver.find_element(By.ID,"tuesday").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,"body > div > div:nth-child(5) > div.card-body > div > select > option:nth-child(3)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"body > div > div:nth-child(5) > div.card-body > div > select > option:nth-child(4)").click()
        time.sleep(10)
        driver.find_element(By.XPATH,"/html/body/div/div[5]/div[2]/div[1]/div[1]/label").click()
        time.sleep(4)
        driver.find_element(By.XPATH,"/html/body/div/div[5]/div[2]/div[2]/div[1]/label").click()
        time.sleep(4)
        driver.find_element(By.XPATH,"/html/body/div/div[5]/div[2]/div[2]/div[4]/label").click()
        time.sleep(4)
        driver.find_element(By.XPATH,"/html/body/div/div[6]/div[2]/div/div/div[1]/label").send_keys("C:/Users/user/Videos/DOK AVC/BA/a.jpeg")
        time.sleep(4)
        driver.find_element(By.XPATH,"/html/body/div/div[6]/div[2]/div/div/div[2]").click()
        time.sleep(4)



    #---------------------------------------------MANUAL BUT AUTOMATION----------------------------------------
    # def test_Login_TC051_Positif(self): 
    #     driver = self.driver
    #     driver.get("https://itera-qa.azurewebsites.net/#") 
    #     driver.maximize_window()
    #     time.sleep(2)
    #     driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(2)").click()
    #     time.sleep(3)
    #     driver.find_element(By.ID,"Username").send_keys("kelompok_13")
    #     time.sleep(3)
    #     driver.find_element(By.ID,"Password").send_keys("kelompok_13")
    #     time.sleep(3)
    #     driver.find_element(By.NAME,"login").click()
    #     time.sleep(3)
    #     driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(3) > a").click()
    #     time.sleep(4)
    #     driver.find_element(By.ID,"name").send_keys(inputan.Name)
    #     time.sleep(2)
    #     driver.find_element(By.ID,"phone").send_keys(inputan.Mobile_number)
    #     time.sleep(2)
    #     driver.find_element(By.ID,"email").send_keys(inputan.Email_address)
    #     time.sleep(2)
    #     driver.find_element(By.ID,"password").send_keys(inputan.Password)
    #     time.sleep(2)
    #     driver.find_element(By.ID,"address").send_keys(inputan.Address)
    #     time.sleep(15)
    #     driver.find_element(By.NAME,"submit").click()
    #     time.sleep(15)

    # def test_TC051_Positif(self): 
    #     driver = self.driver
    #     driver.get("https://itera-qa.azurewebsites.net/#") 
    #     driver.maximize_window()
    #     time.sleep(2)
    #     driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(3) > a").click()
    #     time.sleep(4)

    #     driver.find_element(By.ID,"name").send_keys(inputan.Name)
    #     time.sleep(2)
    #     driver.find_element(By.ID,"phone").send_keys(inputan.Mobile_number)
    #     time.sleep(2)
    #     driver.find_element(By.ID,"email").send_keys(inputan.Email_address)
    #     time.sleep(2)
    #     driver.find_element(By.ID,"password").send_keys(inputan.Password)
    #     time.sleep(2)
    #     driver.find_element(By.ID,"address").send_keys(inputan.Address)
    #     time.sleep(2)
    #     driver.find_element(By.NAME,"submit").click()
    #     time.sleep(2)

    # def test_TC052_none_Positif(self):
    #     driver = self.driver
    #     driver.get("https://itera-qa.azurewebsites.net/#") 
    #     driver.maximize_window()
    #     driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(3) > a").click()
    #     time.sleep(4)
    #     driver.find_element(By.ID,"other").click()
    #     time.sleep(20)


    # def test_TC053_Positif(self):
    #     driver = self.driver
    #     driver.get("https://itera-qa.azurewebsites.net/#") 
    #     driver.maximize_window()
    #     driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(3) > a").click()
    #     time.sleep(4)
    #     driver.find_element(By.ID,"female").click()
    #     time.sleep(5)
    #     driver.find_element(By.ID,"male").click()
    #     time.sleep(20)

    # def test_TC053_Positif(self):
    #     driver = self.driver
    #     driver.get("https://itera-qa.azurewebsites.net/#") 
    #     driver.maximize_window()
    #     driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(3) > a").click()
    #     time.sleep(4)
    #     driver.find_element(By.ID,"monday").click()
    #     time.sleep(5)
    #     driver.find_element(By.ID,"tuesday").click()
    #     time.sleep(20)

    # def test_TC054_Positif(self):
    #     driver = self.driver
    #     driver.get("https://itera-qa.azurewebsites.net/#") 
    #     driver.maximize_window()
    #     driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(3) > a").click()
    #     time.sleep(4)
    #     driver.find_element(By.ID,"male").click()
    #     time.sleep(4)
    #     driver.find_element(By.ID,"monday").click()
    #     time.sleep(4)
    #     driver.find_element(By.ID,"tuesday").click()
    #     time.sleep(20)


    # def test_TC055_Positif(self):
    #     driver = self.driver
    #     driver.get("https://itera-qa.azurewebsites.net/#") 
    #     driver.maximize_window()
    #     driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(3) > a").click()
    #     time.sleep(4)
    #     driver.find_element(By.CSS_SELECTOR,"body > div > div:nth-child(5) > div.card-body > div > select > option:nth-child(3)").click()
    #     time.sleep(2)
    #     driver.find_element(By.CSS_SELECTOR,"body > div > div:nth-child(5) > div.card-body > div > select > option:nth-child(4)").click()
    #     time.sleep(10)


    # def test_TC056and57_Positif(self):
    #     driver = self.driver
    #     driver.get("https://itera-qa.azurewebsites.net/#") 
    #     driver.maximize_window()
    #     driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(3) > a").click()
    #     time.sleep(4)
    #     driver.find_element(By.XPATH,"/html/body/div/div[5]/div[2]/div[1]/div[1]/label").click()
    #     time.sleep(4)
    #     driver.find_element(By.XPATH,"/html/body/div/div[5]/div[2]/div[2]/div[1]/label").click()
    #     time.sleep(4)
    #     driver.find_element(By.XPATH,"/html/body/div/div[5]/div[2]/div[2]/div[4]/label").click()
    #     time.sleep(4)
    
    #def test_TC058_Positif(self):
        # driver = self.driver
        # driver.get("https://itera-qa.azurewebsites.net/#") 
        # driver.maximize_window()
        # driver.find_element(By.CSS_SELECTOR,"#navbarColor01 > ul > li:nth-child(3) > a").click()
        # time.sleep(4)
        # driver.find_element(By.XPATH,"/html/body/div/div[6]/div[2]/div/div/div[1]/label").click()
        # driver.find_element(By.XPATH,"/html/body/div/div[6]/div[2]/div/div/div[1]/label").send_keys("C:/Users/user/Videos/DOK AVC/BA/a.jpeg")
        # time.sleep(4)
        # driver.find_element(By.XPATH,"/html/body/div/div[6]/div[2]/div/div/div[2]").click()
        # time.sleep(4)


        #HARUSNYA BISA PAKE PERINTAH INI
        #driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm") 
        #driver.maximize_window()
        # s = driver.find_element(By.XPATH,"//input[@type='file']")
        # s.send_keys("C:/Users/user/Videos/DOK AVC/BA/a.jpeg")
        # time.sleep(20)

unittest.main()