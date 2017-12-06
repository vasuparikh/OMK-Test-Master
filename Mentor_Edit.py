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
        elem = driver.find_element_by_xpath(
            "/html/body/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[7]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_Mentor_name").clear()
        time.sleep(2)
        elem = driver.find_element_by_id("id_Mentor_name")
        elem.send_keys("Vaishnavi")

        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(3)
        driver.get("https://om4k-1.herokuapp.com/mentorlist/")

        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
