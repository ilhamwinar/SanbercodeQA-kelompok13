import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from data_input import inputan,inputan2
from selenium.webdriver.common.action_chains import ActionChains


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
        
        response_dashboard=driver.find_element(By.XPATH,"/html/body/div").text
        time.sleep(10)
        if "Dashboard" in response_dashboard:
            print("PASSED")
        else:
            print('NOT PASSED')

        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div/p[1]/a").click()
        time.sleep(3)
        driver.find_element(By.ID,"Name").send_keys(inputan.Name)
        time.sleep(3)
        driver.find_element(By.ID,"Company").send_keys(inputan.Company)
        time.sleep(3)
        driver.find_element(By.ID,"Address").send_keys(inputan.Address)
        time.sleep(3)
        driver.find_element(By.ID,"City").send_keys(inputan.City)
        time.sleep(3)
        driver.find_element(By.ID,"Phone").send_keys(inputan.Phone)
        time.sleep(3)
        driver.find_element(By.ID,"Email").send_keys(inputan.Email)
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input").click()
        time.sleep(10)
        
        response_table=driver.find_element(By.XPATH,"/html/body/div/div/table").text
        time.sleep(60)
        if (inputan.Name and inputan.Company and inputan.Address and inputan.City and inputan.Phone and inputan.Email ) in response_table:
            print("PASSED")
        else:
            print('NOT PASSED')

        #backtolist
        driver.find_element(By.XPATH,"/html/body/div/div/p[1]/a").click()
        driver.find_element(By.XPATH,"/html/body/div/div/a").click()
        time.sleep(3)

        response_dashboard=driver.find_element(By.XPATH,"/html/body/div").text
        time.sleep(10)
        if "Dashboard" in response_dashboard:
            print("PASSED")
        else:
            print('NOT PASSED')

        # time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[1]").click()
        driver.find_element(By.ID,"Name").clear()
        driver.find_element(By.ID,"Company").clear()
        driver.find_element(By.ID,"Address").clear()
        driver.find_element(By.ID,"City").clear()
        driver.find_element(By.ID,"Phone").clear()
        driver.find_element(By.ID,"Email").clear()
        time.sleep(3)
        driver.find_element(By.ID,"Name").send_keys(inputan2.Name)
        time.sleep(3)
        driver.find_element(By.ID,"Company").send_keys(inputan2.Company)
        time.sleep(3)
        driver.find_element(By.ID,"Address").send_keys(inputan2.Address)
        time.sleep(3)
        driver.find_element(By.ID,"City").send_keys(inputan2.City)
        time.sleep(3)
        driver.find_element(By.ID,"Phone").send_keys(inputan2.Phone)
        time.sleep(3)
        driver.find_element(By.ID,"Email").send_keys(inputan2.Email)
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input").click()
        time.sleep(10)
        
        response_table2=driver.find_element(By.XPATH,"/html/body/div/div/table").text
        time.sleep(60)
        if (inputan2.Name and inputan2.Company and inputan2.Address and inputan2.City and inputan2.Phone and inputan2.Email ) in response_table2:
            print("PASSED")
        else:
            print('NOT PASSED')
        
        #TC033
        driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[1]").click()
        driver.find_element(By.ID,"Name").clear()
        driver.find_element(By.ID,"Company").clear()
        driver.find_element(By.ID,"Address").clear()
        driver.find_element(By.ID,"City").clear()
        driver.find_element(By.ID,"Phone").clear()
        driver.find_element(By.ID,"Email").clear()
        driver.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input").click()
        time.sleep(10)

        response_table2=driver.find_element(By.XPATH,"/html/body/div/div/table").text
        time.sleep(60)
        if "" in response_table2:
            print("PASSED")
        else:
            print('NOT PASSED')

        #TC035
        driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[1]").click()
        driver.find_element(By.ID,"Name").clear()
        driver.find_element(By.ID,"Company").clear()
        driver.find_element(By.ID,"Address").clear()
        driver.find_element(By.ID,"City").clear()
        driver.find_element(By.ID,"Phone").clear()
        driver.find_element(By.ID,"Email").clear()
        driver.find_element(By.XPATH,"/html/body/div/form/div/div[7]/div/input").click()
        time.sleep(10)

        #TC034
        # driver.find_element(By.ID,"Phone").send_keys("Halo")
        # time.sleep(3)
        # response_table2=driver.find_element(By.XPATH,"/html/body/div/div/table").text
        # time.sleep(60)
        # if "" in response_table2:
        #     print("PASSED")
        # else:
        #     print('NOT PASSED')

        #TC036
        driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div/a").click()
        time.sleep(5)

        #TC035
        driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/p/a[2]").click()
        time.sleep(5)

        # #TC037
        driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[3]").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div/form/div/input").click()
        time.sleep(3)

        # TC038
        driver.find_element(By.XPATH,"//*[@id='searching']").send_keys(inputan.Email)
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div/form/input[2]").click()
        
        ## TC039
        driver.find_element(By.XPATH,"//*[@id='searching']").clear
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='searching']").send_keys(inputan2.Email)
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div/form/input[2]").click()
        time.sleep(10)
        
        
        driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr[2]/td[7]/a[3]")
        actions = ActionChains(driver)
        actions.perform()
        time.sleep(10)

unittest.main()