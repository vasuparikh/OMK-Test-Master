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
        time.sleep(2)
        driver.get("https://om4k-1.herokuapp.com/mentorlist/")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[2]/div/a/span").click()
        time.sleep(2)

        elem = driver.find_element_by_id("id_Mentor_Id")
        elem.send_keys("M_012")
        time.sleep(1)
        elem = driver.find_element_by_id("id_Mentor_name")
        elem.send_keys("Shamrose")

        elem = driver.find_element_by_id("id_Mentor_phone")
        elem.send_keys("9314887519")
        elem = driver.find_element_by_id("id_Mentor_Address")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_id("id_Mentor_Gender")
        elem.send_keys("M")
        elem = driver.find_element_by_id("id_begining_date").clear()
        time.sleep(2)
        elem = driver.find_element_by_id("id_begining_date")
        elem.send_keys("2017-12-01")

        elem = driver.find_element_by_id("id_Mentor_email")
        elem.send_keys("smakandar@unomaha.edu")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(3)
        driver.get("https://om4k-1.herokuapp.com/mentorlist/")

        assert "Mentor Added"

        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
