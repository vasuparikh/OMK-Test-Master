import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class OMK_Mentorlogin(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_mentorLoginInvalid(self):
       user = "Ranji"
       pwd = "test1234"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://om4k-1.herokuapp.com/login_user/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       assert "Invalid Login"
       time.sleep(5)

   def test_mentorLoginValid(self):
       user = "Ranjitha"
       pwd = "ranji12345"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://om4k-1.herokuapp.com/login_user/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       assert "Logged In"
       time.sleep(5)
       # Click Student List
       elem = driver.find_element_by_xpath("//*[@id='wrapper']/nav/div[2]/ul/li[3]/a").click()
       # Click Student Reports
       elem = driver.find_element_by_xpath("//*[@id='wrapper']/nav/div[2]/ul/li[4]/a").click()
       # Edit a Student
       elem = driver.find_element_by_xpath("//*[@id='page-wrapper']/div/div/div/table/tbody/tr[1]/td[7]/a").click()
       elem = driver.find_element_by_id("id_Comments")
       elem.clear()
       elem.send_keys("Showing Improvement")
       elem = driver.find_element_by_xpath("//*[@id='page-wrapper']/div/form/button").click()
       time.sleep(5)
       assert "Edited the Student Comment"
       time.sleep(5)



   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
