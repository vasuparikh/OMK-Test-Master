import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_OMK(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_omk_mentor(self):
       user = "Ranjitha"
       pwd = "ranji12345"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/")
       time.sleep(2)
       driver.get("http://127.0.0.1:8000/login_user/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       driver.get("http://127.0.0.1:8000/mentorhome/")
       assert "Logged In"
       time.sleep(1)
       driver.get("http://127.0.0.1:8000/studentsreports")
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr[1]/td[7]/a").click()
       driver.get("http://127.0.0.1:8000/studentsreportsedit/8/edit/")
       elem = driver.find_element_by_id("id_Student_curr_grade").clear()
       elem = driver.find_element_by_id("id_Student_curr_grade")
       elem.send_keys("B")
       elem = driver.find_element_by_id("id_Parents_phone").clear()
       elem = driver.find_element_by_id("id_Parents_phone")
       elem.send_keys("5714200041")
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
       time.sleep(2)
       driver.get("http://127.0.0.1:8000/studentsreports")
       assert "Student Report Updated"
       time.sleep(2)


   def tearDown(self):
       self.driver.close()