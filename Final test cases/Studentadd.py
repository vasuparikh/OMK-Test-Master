# Create your tests here.
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Employee_Login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_about_us(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://om4k-1.herokuapp.com")
       driver.find_element_by_link_text("About Us").click()

   def test_Login_user(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://om4k-1.herokuapp.com")
       elem = driver.find_element_by_link_text("Login").click()
       elem = driver.find_element_by_id("id_username")
       elem.send_keys("Sravani")
       elem = driver.find_element_by_id("id_password")
       elem.send_keys("srav12345")
       driver.find_element_by_xpath("//button[contains(.,'Submit')]").click()

   def test_Add_students(self):
       user = "ID"
       pwd = "PW"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://om4k-1.herokuapp.com")
       elem=driver.find_element_by_link_text("Login").click()
       elem = driver.find_element_by_id("id_username")
       elem.send_keys("Sravani")
       elem = driver.find_element_by_id("id_password")
       elem.send_keys("srav12345")
       driver.find_element_by_xpath("//button[contains(.,'Submit')]").click()
       # Click Student List
       elem = driver.find_element_by_xpath("//*[@id='wrapper']/nav/div[2]/ul/li[2]/a").click()
       #Click Add Student
       elem = driver.find_element_by_xpath("//*[@id='page-wrapper']/div/div/div/a/span").click()
       # "Opened Page to Add Mentor"
       elem = driver.find_element_by_id("id_Student_id")
       elem.send_keys("s_10")
       elem = driver.find_element_by_id("id_Student_name")
       elem.send_keys("Samaira")
       elem = driver.find_element_by_id("id_Student_curr_grade")
       elem.send_keys("B")
       elem = driver.find_element_by_id("id_Student_prev_grade")
       elem.send_keys("C")
       elem = driver.find_element_by_id("id_Student_Class")
       elem.send_keys("9")
       elem = driver.find_element_by_id("id_Parents_email")
       email= "samaira@gmail.com"
       elem.send_keys(email)
       elem = driver.find_element_by_id("id_Parents_phone")
       elem.send_keys("4025143673")
       elem = driver.find_element_by_id("id_School")
       elem.send_keys("UNO Omaha")
       elem = Select(driver.find_element_by_id("id_Men_name"))
       elem.select_by_value("2")
       elem = Select(driver.find_element_by_id("id_Emp_name"))
       elem.select_by_value("1")
       elem = driver.find_element_by_id("id_Comments")
       elem.send_keys("Need to guide him about Future options")
       # time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='page-wrapper']/div/form/button").click()
       time.sleep(5)


   def test_Log_out(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://om4k-1.herokuapp.com")
       elem = driver.find_element_by_link_text("Login").click()
       elem = driver.find_element_by_id("id_username")
       elem.send_keys("Sravani")
       elem = driver.find_element_by_id("id_password")
       elem.send_keys("srav12345")
       driver.find_element_by_xpath("//button[contains(.,'Submit')]").click()
       driver.find_element_by_partial_link_text("Hello Sravani").click()
       #time.sleep(10)
       driver.find_element_by_partial_link_text("Log Out").click()
       #time.sleep(10)


   def tearDown(self):
       self.driver.close()


if __name__ == "__main__":
   unittest.main()

