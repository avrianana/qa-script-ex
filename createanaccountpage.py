import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Webdriver(unittest.TestCase):
    def setUp(self):
        # test open web browser with chrome
        self.driver = webdriver.Chrome()
        # test open web browser with firefox
        # self.driver = webdriver.Firefox()
        # test open web browser with safari
        # self.driver = webdriver.Safari()
        # test open web browser with edge
        # self.driver = webdriver.Edge()
        print("success open web browser")

    def test_url_function(self):
        driver = self.driver
        driver.get("http://reviews.femaledaily.net/")
        driver.set_page_load_timeout(2)
        driver.maximize_window()
        # driver.set_window_size(1341, 810)
        driver.implicitly_wait(2)
        time.sleep(2)
        print("success open website reviews.femaledaily.net")

        # test click login/signup
        elem = driver.find_element_by_xpath("//span[@class='gbheader-profile']")
        elem.click()
        time.sleep(2)
        print("setup click login/signup")
        # test click create an account
        elem = driver.find_element(By.XPATH, '//button[text()="CREATE AN ACCOUNT"]')
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        print("setup click create an account")

        # test input email, username, password
        elem = driver.find_element_by_xpath("//input[@placeholder='Email']")
        elem.send_keys("dumdummy@gmail.com")
        time.sleep(2)
        print("setup email is true")
        elem = driver.find_element_by_xpath("//input[@placeholder='Username']")
        elem.send_keys("dumdummy")
        time.sleep(2)
        print("setup username is true")
        elem = driver.find_element_by_xpath("//input[@placeholder='Password']")
        elem.send_keys("avind987")
        time.sleep(2)
        print("setup password is true")
        # test click to check box for terms & conditions
        elem = driver.find_element_by_xpath("//label[@class='modal-register-input-agreement']")
        elem.click()
        time.sleep(2)
        print("setup click check box for terms & condition")
        # test click to submit create new account
        elem = driver.find_element_by_xpath("//input[@value='CREATE NEW ACCOUNT']")
        elem.click()
        time.sleep(8)
        print("setup click to submit create new account")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
