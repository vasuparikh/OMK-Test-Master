import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_OMK(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()
# Employee Login to the OMK website.
   def test_omk_employee(self):
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
       time.sleep(2)
  # Search for student using their name.    
       search= driver.find_element_by_name("name")
       elem=driver.find_element_by_xpath("/html/body/div/div/div/div[1]/form/div/input[1]")
       elem.send_keys("Nikesh")
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       assert "Student Record Found"
       time.sleep(3)
       driver.get("https://om4k-1.herokuapp.com/emphome/")
       time.sleep(2)
   # Search for students who got B+ in their current       
       search = driver.find_element_by_name("currgrade")
       elem=driver.find_element_by_xpath("/html/body/div/div/div/div[1]/form/div/input[2]")
       search.send_keys("B+")
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(1)
       driver.get("https://om4k-1.herokuapp.com/emphome/")
       time.sleep(2)
    # Search for student who got A in their current grade and F as in their previous grade     
       search = driver.find_element_by_name("currgrade")
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/form/div/input[2]")
       search.send_keys("A")
       search = driver.find_element_by_name("prevgrade")
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/form/div/input[3]")
       search.send_keys("F")
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(2)


   def tearDown(self):
       self.driver.close()
