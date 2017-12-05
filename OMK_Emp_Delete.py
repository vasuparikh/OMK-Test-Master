import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_OMK(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_omk_mentor(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://om4k-1.herokuapp.com/admin/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       #driver.get("https://om4k-1.herokuapp.com/admin/")
       assert "Logged In"
       time.sleep(2)

       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/th/a").click()
       #driver.get("http://127.0.0.1:8000/admin/auth/user/")
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[7]/th/a").click()
       time.sleep(2)
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/p/a").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
       time.sleep(2)
       #driver.get("https://om4k-1.herokuapp.com/admin/")
       elem=driver.find_element_by_xpath("/html/body/div/div[2]/a[1]").click()
       time.sleep(2)





       #elem= driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/label/select/option[2]").click()
       #driver.get("http://127.0.0.1:8000/admin/auth/user/21/change/")
       #time.sleep(2)
       #elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/p/a").click()
       #time.sleep(2)
       #driver.get("http://127.0.0.1:8000/admin/auth/user/21/delete/")
       #time.sleep(2)
       #elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
       #time.sleep(1)
       #driver.get("http://127.0.0.1:8000/admin/")
       #time.sleep(3)




       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[3]/th/a").click()
       time.sleep(2)
       #driver.get("http://127.0.0.1:8000/admin/home/employee/")
       #time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
       time.sleep(2)
       #driver.get("http://127.0.0.1:8000/admin/home/employee/21/change/")
       #time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/p/a").click()
       #driver.get("http://127.0.0.1:8000/admin/home/employee/21/delete/")
       #time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
       time.sleep(2)
       elem= driver.find_element_by_xpath("/html/body/div/div[2]/a[1]").click()
       #driver.get("https://om4k-1.herokuapp.com/admin/")
       time.sleep(3)




   def tearDown(self):
       self.driver.close()