import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class OMK_Admin(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_superuserloginInvalid(self):
       user = "instructor"
       pwd = "instructor"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://om4k-1.herokuapp.com/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       assert "Incorrect Username and password"
       time.sleep(2)

   def test_superuserloginValid(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://om4k-1.herokuapp.com/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       assert "Logged In"
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='content-main']/div[2]/table/tbody/tr[3]/td[1]/a").click()
       time.sleep(3)
       assert "Opened Page to Add Mentor"
       elem = driver.find_element_by_id("id_Mentor_Id")
       elem.send_keys("m_11")
       elem = driver.find_element_by_id("id_Mentor_name")
       elem.send_keys("MentorAutomatedTestFinal")
       elem = driver.find_element_by_id("id_Mentor_phone")
       elem.send_keys("1234567890")
       email="Automatedtest@gmail.com"
       elem = driver.find_element_by_id("id_Mentor_email")
       elem.clear()
       elem.send_keys(email)
       #time.sleep(5)
       elem = driver.find_element_by_id("id_Mentor_Address")
       elem.send_keys("UNO Omaha")
       elem = driver.find_element_by_id("id_Mentor_Gender")
       elem.clear()
       elem.send_keys("F")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='mentor_form']/div/div/input[1]").click()
       time.sleep(2)
       assert "Created a Mentor"

       # Editing the Mentor
       driver.get("https://om4k-1.herokuapp.com/admin")
       elem = driver.find_element_by_xpath("//*[@id='content-main']/div[2]/table/tbody/tr[3]/td[2]/a").click()
       time.sleep(2)
       assert "Opened Page to Edit Mentor"
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='result_list']/tbody/tr[1]/th/a").click()
       elem = driver.find_element_by_id("id_Mentor_name")
       elem.clear()
       elem.send_keys("MentorTest12updatedFinal")
       elem = driver.find_element_by_xpath("//*[@id='mentor_form']/div/div/input[1]").click()
       time.sleep(3)
       assert "Edited the Mentor"
       time.sleep(5)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
