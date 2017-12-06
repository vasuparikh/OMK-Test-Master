import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_Stud_Rep(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_stud_rep_edit(self):
       user = "Sravani"
       pwd = "srav12345"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://om4k-1.herokuapp.com/login_user/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/nav/div[2]/ul/li[4]/a").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr[1]/td[7]/a").click()
       time.sleep(2)

       elem = driver.find_element_by_id("id_Student_curr_grade").clear()
       time.sleep(1)
       elem = driver.find_element_by_id("id_Student_curr_grade")
       elem.send_keys("B")

       elem = driver.find_element_by_id("id_Parents_phone").clear()
       time.sleep(1)
       elem = driver.find_element_by_id("id_Parents_phone")
       elem.send_keys("5714455233")

       elem = driver.find_element_by_id("id_Comments").clear()
       time.sleep(1)
       elem = driver.find_element_by_id("id_Comments")
       elem.send_keys("Way to go!")

       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()

       time.sleep(5)



       # elem= driver.find_element_by_xpath("").click()

       def tearDown(self):
           self.driver.close()
