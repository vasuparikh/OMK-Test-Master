import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_OMK(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()
# login in to OMK Website as an employee.
   def test_omk_mentor(self):
       user = "Sravani"
       pwd = "srav12345"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://om4k-1.herokuapp.com/")
       time.sleep(2)
       driver.get("https://om4k-1.herokuapp.com/login_user/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       driver.get("https://om4k-1.herokuapp.com/emphome/")
       assert "Logged In"
       time.sleep(1)
       # Goto students repot, update the current grade and parents phone number
       elem = driver.find_element_by_xpath("/html/body/div/nav/div[2]/ul/li[4]/a").click()
       driver.get("https://om4k-1.herokuapp.com/empstudentsreports/")
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr[4]/td[7]/a").click()
       driver.get("https://om4k-1.herokuapp.com/empstudreportedit/8/edit/")
       time.sleep(2)
       elem = driver.find_element_by_id("id_Student_curr_grade").clear()
       elem = driver.find_element_by_id("id_Student_curr_grade")
       elem.send_keys("B")
       elem = driver.find_element_by_id("id_Parents_phone").clear()
       elem = driver.find_element_by_id("id_Parents_phone")
       elem.send_keys("5714200041")
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
       time.sleep(2)
       driver.get("https://om4k-1.herokuapp.com/empstudreportedit/8/edit")
       time.sleep(2)
       driver.get("https://om4k-1.herokuapp.com/empstudentsreports/")
       assert "Student Report Updated"
       time.sleep(2)


   def tearDown(self):
       self.driver.close()
