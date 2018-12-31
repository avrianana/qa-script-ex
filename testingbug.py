import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint


class Webdriver(unittest.TestCase):
    def setUp(self):
        # test open web browser with firefox
        # self.driver = webdriver.Firefox()
        # test open web browser with chrome
        self.driver = webdriver.Chrome()
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

        # test random menu bar
        print("Random Menu Bar")
        # test click to random menu bar for menu bar
        elem = driver.find_elements_by_css_selector('div.gtmenu-menu-text')
        # create a list and chose a random menu bar
        menubar = elem[randint(0, len(elem) - 1)]
        menubar.click()
        time.sleep(5)
        print("success click to random menu bar")
        driver.execute_script("window.scrollBy(0,200);")
        time.sleep(5)
        print("success smooth scrolling through the page")

        # RANDOM FILTER BY CATEGORY
        print("RANDOM FILTER BY CATEGORY")
        # test click to random filter by category
        elem = driver.find_elements_by_css_selector('div.jsx-17482050.filter-category-desktop')
        # create a list and chose a random filter by category
        fbc = elem[randint(0, len(elem) - 1)]
        fbc.click()
        time.sleep(5)
        print("setup click to random filter by category")
        driver.execute_script("window.scrollBy(0,200);")
        time.sleep(2)
        print("setup smooth scrolling through the page")

        # RANDOM FILTER BY CATEGORY
        print("RANDOM FILTER BY CATEGORY")
        # test click to random filter by category
        elem = driver.find_elements_by_css_selector('div.jsx-17482050.filter-category-desktop')
        # create a list and chose a random filter by category
        fbc = elem[randint(0, len(elem) - 1)]
        fbc.click()
        time.sleep(5)
        print("setup click to random filter by category")
        driver.execute_script("window.scrollBy(0,200);")
        time.sleep(2)
        print("setup smooth scrolling through the page")

        def tearDown(self):
            self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
