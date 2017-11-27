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
       id = "E_003"
       ename = "Stacy"
       ephone = "5697841236"
       email = "stacyk@gmail.com"
       eaddress = "Omaha"
       uname = "Stacy"
       pwd1 = "hello12345"
       pwd2 = "hello12345"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       driver.get("http://127.0.0.1:8000/admin")
       assert "Logged In"
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/th/a").click()
       time.sleep(1)
       driver.get("http://127.0.0.1:8000/admin/home/employee/")
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
       driver.get("http://127.0.0.1:8000/admin/home/employee/add/")
       time.sleep(3)
       elem = driver.find_element_by_id("id_Employee_Id")
       elem.send_keys(id)
       elem = driver.find_element_by_id("id_Employee_name")
       elem.send_keys(ename)
       elem = driver.find_element_by_id("id_Employee_phone")
       elem.send_keys(ephone)
       elem = driver.find_element_by_id("id_Employee_email")
       elem.send_keys(email)
       elem = driver.find_element_by_id("id_Employee_Address")
       elem.send_keys(eaddress)
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]").click()
       time.sleep(2)
       driver.get("http://127.0.0.1:8000/admin/home/employee/")
       time.sleep(2)
       driver.get("http://127.0.0.1:8000/admin/")
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[1]/a").click()
       #driver.get("http://127.0.0.1:8000/admin/auth/user/")
       #time.sleep(2)
       #elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
       driver.get("http://127.0.0.1:8000/admin/auth/user/add/")
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(uname)
       elem = driver.find_element_by_id("id_password1")
       elem.send_keys(pwd1)
       elem = driver.find_element_by_id("id_password2")
       elem.send_keys(pwd2)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]").click()
       #time.sleep(2)
       #driver.get("http://127.0.0.1:8000/admin/")
       #driver.get("http://127.0.0.1:8000/admin/auth/user/")
       #time.sleep(2)
       #elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[8]/th/a").click()
       driver.get("http://127.0.0.1:8000/admin/auth/user/21/change/")
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys(uname)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys(email)
       time.sleep(1)
       elem = driver.find_element_by_id("id_is_staff").click()
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
       time.sleep(2)
       driver.get("http://127.0.0.1:8000/admin/")
       time.sleep(5)

       #driver.get("http://127.0.0.1:8000/admin/home/employee/")
       #time.sleep(2)
       #elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
       #time.sleep(1)
       #driver.get("http://127.0.0.1:8000/admin/home/employee/13/change/")
       #time.sleep(2)
       #elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/p/a").click()
       #driver.get("http://127.0.0.1:8000/admin/home/employee/13/delete/")
       #time.sleep(1)
       #elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
       #driver.get("http://127.0.0.1:8000/admin/home/employee/")




   def tearDown(self):
       self.driver.close()