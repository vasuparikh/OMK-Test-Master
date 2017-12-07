#By Ranjitha
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Test_OMK_search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Employee Login to the OMK website.
    def test_omk_employee(self):
        user = "Sravani"
        pwd = "srav12345"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://om4k-1.herokuapp.com/")
        #time.sleep(2)
        driver.get("https://om4k-1.herokuapp.com/login_user/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        #time.sleep(2)
        elem.send_keys(Keys.RETURN)
        # driver.get("https://om4k-1.herokuapp.com/emphome/")
        assert "Logged In"

        #time.sleep(2)
        # Search for student using their name.
        elem = driver.find_element_by_name("name")
        student = "Rina"
        elem.send_keys(student)
        elem = driver.find_element_by_xpath("//*[@id='page-wrapper']/div/div[1]/form/button").click()
        time.sleep(5)
        #elem.send_keys(Keys.RETURN)
        assert "Student Record Found"
        #time.sleep(3)

    def tearDown(self):
     self.driver.close()


if __name__ == "__main__":
   unittest.main()
