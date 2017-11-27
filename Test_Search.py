import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_OMK(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()
# Enter the OMK website as a mentor.
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
       time.sleep(2)
   # Search for student by name Goutham   
       search= driver.find_element_by_name("name")
       search.send_keys("Goutham")
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/form/button").click()
       driver.get("http://127.0.0.1:8000/searchment/?name=Goutham&currgrade=&prevgrade=")
       assert "Student Record Found"
       time.sleep(3)
       driver.get("http://127.0.0.1:8000/mentorhome/")
       time.sleep(2)
    # Search by student Cuurent Grade "A"  
       search = driver.find_element_by_name("currgrade")
       search.send_keys("A")
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/form/button").click()
       time.sleep(1)
       driver.get("http://127.0.0.1:8000/searchment/?name=&currgrade=A&prevgrade=")
       time.sleep(3)
       driver.get("http://127.0.0.1:8000/mentorhome/")
       time.sleep(2)
    # Search by student cuurent grade "A" and previous grade "F".  
       search = driver.find_element_by_name("currgrade")
       search.send_keys("A")
       search = driver.find_element_by_name("prevgrade")
       search.send_keys("F")
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/form/button").click()
       time.sleep(1)
       driver.get("http://127.0.0.1:8000/searchment/?name=&currgrade=A&prevgrade=F")
       time.sleep(2)

   def tearDown(self):
       self.driver.close()
