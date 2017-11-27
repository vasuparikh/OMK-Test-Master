from django.test import TestCase

# Create your tests here.
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlrd

class Employee_Login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe")

   def test_about_us(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/")
       driver.find_element_by_link_text("About Us").click()

   def test_Login_user(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/")
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
       driver.get("http://127.0.0.1:8000/")
       elem=driver.find_element_by_link_text("Login").click()
       elem = driver.find_element_by_id("id_username")
       elem.send_keys("Sravani")
       elem = driver.find_element_by_id("id_password")
       elem.send_keys("srav12345")
       driver.find_element_by_xpath("//button[contains(.,'Submit')]").click()
       #elem=driver.find_element_by_class_name("fa fa-user")
       #elem.find_elements_by_css_selector('a').get_attribute('href').click()
       #elem.send_keys(Keys.RETURN)
       #driver.get("http://127.0.0.1:8000")
       #assert "Log In"
       time.sleep(10)
       #driver.find_element_by_partial_link_text("Hello Sravani").click()
       #time.sleep(5)
       #driver.find_element_by_partial_link_text("Log Out").click()
       driver.find_element_by_partial_link_text("Student List").click()
       # Add student driver.find_element_by_class_name("btn-primary").click()
       book  = xlrd.open_workbook("C:/Python/Sprint2/OMK-7/Input.xlsx")
       first_sheet = book.sheet_by_index(0)
       #Username= first_sheet.cell(1,0)
       #Password=first_sheet.cell(1,1)
       #print(Username)
       #print(Password)
      # men_name=str(first_sheet.cell(1,8).value)
      # emp_name=str(first_sheet.cell(1,9).value)
       #men_name="Ishma"
       print("jhbjhbschj")
      # print(men_name)
       row = first_sheet.nrows
       print(row)
       for rows in range(1,first_sheet.nrows) :
            driver.find_element_by_class_name("btn-primary").click()
            men_name = str(first_sheet.cell(rows, 8).value)
            emp_name = str(first_sheet.cell(rows, 9).value)
            driver.find_element_by_id("id_Student_id").send_keys(first_sheet.cell(rows,0).value)
            #driver.find_element_by_id("id_Student_id").first_sheet.cell(rows, 0).value
            driver.find_element_by_id("id_Student_name").send_keys(first_sheet.cell(rows,1).value)
            elem= driver.find_element_by_id("id_Student_curr_grade")
            elem.send_keys(Keys.CONTROL + "a")
            elem.send_keys(Keys.CLEAR)
            driver.find_element_by_id("id_Student_curr_grade").send_keys(first_sheet.cell(rows,2).value)
            elem= driver.find_element_by_id("id_Student_prev_grade")
            elem.send_keys(Keys.CONTROL + "a")
            elem.send_keys(Keys.CLEAR)
            driver.find_element_by_id("id_Student_prev_grade").send_keys(first_sheet.cell(rows, 3).value)
            driver.find_element_by_id("id_Student_Class").send_keys(int(first_sheet.cell(rows,4).value))
            elem=driver.find_element_by_id("id_Parents_email")
            elem.send_keys(Keys.CONTROL + "a")
            elem.send_keys(Keys.CLEAR)
            driver.find_element_by_id("id_Parents_email").send_keys(first_sheet.cell(rows,5).value)
            driver.find_element_by_id("id_Parents_phone").send_keys(str(first_sheet.cell(rows, 6).value))
            driver.find_element_by_id("id_School").send_keys(str(first_sheet.cell(rows, 7).value))
            driver.find_element_by_id("id_Men_name").send_keys(men_name)
            #driver.find_element_by_xpath("//select[@id='id_Men_name']/option[@value= '4']").click()
            #driver.find_element_by_id("id_Emp_name").send_keys(first_sheet.cell(rows, 8).value)
            driver.find_element_by_id("id_Emp_name").send_keys(emp_name)
            #driver.find_element_by_id("id_last_date").send_keys(first_sheet.cell(rows, 8).value)
            #driver.find_elements_by_class_name("btn-default").click()
            #driver.find_element_by_partial_link_text("Save").click()
            time.sleep(10)
            driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()


            time.sleep(2)
            driver.get("http://127.0.0.1:8000/studentlist/")
            time.sleep(2)

   def test_Log_out(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/")
       elem = driver.find_element_by_link_text("Login").click()
       elem = driver.find_element_by_id("id_username")
       elem.send_keys("Sravani")
       elem = driver.find_element_by_id("id_password")
       elem.send_keys("srav12345")
       driver.find_element_by_xpath("//button[contains(.,'Submit')]").click()
       driver.find_element_by_partial_link_text("Hello Sravani").click()
       time.sleep(10)
       driver.find_element_by_partial_link_text("Log Out").click()
       time.sleep(10)
     #def Add_student(self):




       def tearDown(self):
           self.driver.close()

   if __name__ == "__main__":
       unittest.main()

