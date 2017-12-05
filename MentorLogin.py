import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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

   def test_mark_attendance(self):
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

       #Mark Attendance
       elem = driver.find_element_by_xpath("//*[@id='wrapper']/nav/div[2]/ul/li[2]/a").click()
       elem = driver.find_element_by_xpath("//*[@id='page-wrapper']/div/div/div/table/tbody/tr[1]/td[3]/a").click()
       #elem = driver.find_element_by_name("stu_name").click()
       elem = Select(driver.find_element_by_id("id_stu_name"))
       elem.select_by_value("2")
       elem = driver.find_element_by_id("id_attend").click()
       elem = driver.find_element_by_id("id_remarks")
       elem.clear()
       elem.send_keys("This is test Attendance")
       elem = driver.find_element_by_xpath("//*[@id='page-wrapper']/div/form/button").click()

       # Click Student List
       elem = driver.find_element_by_xpath("//*[@id='wrapper']/nav/div[2]/ul/li[3]/a").click()



   def test_edit_student(self):
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
