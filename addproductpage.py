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

        # test click menu bar add product
        print("Menu Bar Add Product")
        elem = driver.find_element_by_xpath("//span[@class='gbheader-add']")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        time.sleep(2)
        print("success mouse hover menu bar add product")
        # test click add product
        print("Add Product")
        elem = driver.find_element(By.XPATH, '//a[text()="Add Product"]')
        elem.click()
        time.sleep(2)
        print("success click add product")

        # test login an account
        print("Login Account")
        # test click username and password
        print("Username and Password")
        elem = driver.find_element_by_xpath("//input[@placeholder='Email / Username']")
        elem.send_keys("putwid")
        time.sleep(2)
        print("success username is true")
        elem = driver.find_element_by_xpath("//input[@placeholder='Password']")
        elem.send_keys("tester123")
        time.sleep(2)
        print("success password is true")
        # test click login button
        print("Login Button")
        elem = driver.find_element_by_xpath("//input[@value='LOGIN']")
        elem.click()
        time.sleep(2)
        print("success click to login")

        # test click menu bar add product
        print("Menu Bar Add Product")
        elem = driver.find_element_by_xpath("//span[@class='gbheader-add']")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        time.sleep(2)
        print("success mouse hover menu bar add product")
        # test click add product
        print("Add Product")
        elem = driver.find_element(By.XPATH, '//a[text()="Add Product"]')
        elem.click()
        time.sleep(2)
        print("success click add product")

        # test upload product image
        print("Upload Product Image")
        # test for upload photo
        driver.execute_script("window.scrollBy(0,200);")
        time.sleep(2)
        # elem = driver.find_element(By.XPATH, '//span[class()="ap-btn-upload-ic"]')
        # elem.click()
        # time.sleep(2)
        # print("setup click to upload photo ")
        # test for insert photo
        print("Insert Image")
        elem = driver.find_element_by_xpath("//input[@placeholder='Insert Image url']")
        elem.send_keys("https://img.benefitcosmetics.com/image/upload/f_auto,q_auto,fl_lossy/origin_files/uk/en-gb/sites/uk/files/styles/category_page_lg/public/boi-ing-airbrush-concealer-component.png?itok=L0-xF5mD")
        time.sleep(2)
        print("success insert image url")
        # test for click show image
        elem = driver.find_element(By.XPATH, '//button[text()="show"]')
        elem.click()
        time.sleep(2)
        print("success click show to see image")
        driver.execute_script("window.scrollBy(0,200);")
        time.sleep(2)
        # test for click next
        print("Next")
        elem = driver.find_element_by_xpath("//input[@value='NEXT']")
        elem.click()
        time.sleep(2)
        print("success click next")

        # Upload Product Brand And Name
        print("Upload Product Brand And Name")
        driver.execute_script("window.scrollBy(0,-200);")
        time.sleep(2)
        # test for brand name
        print("Brand Name")
        elem = driver.find_elements_by_css_selector('div.Select-control')
        # create a list and chose a random brand name
        bn = elem[randint(0, len(elem) - 1)]
        bn.click()
        time.sleep(2)
        # test click to random brand name
        elem = driver.find_elements_by_css_selector('div.Select-menu-outer')
        # create a list and chose a random brand name drop down
        bnd = elem[randint(0, len(elem) - 1)]
        bnd.click()
        time.sleep(2)
        print("success click to choose brand name")
        # # test clear box
        # elem = driver.find_element_by_xpath("//span[@class='Select-clear']")
        # elem.click()
        # time.sleep(2)
        # print("Clear Box")
        # test click to random product category
        print("Product Category")
        elem = driver.find_elements_by_css_selector('div.Select-control')
        # create a list and chose a random product category
        ds = elem[randint(0, len(elem) - 1)]
        ds.click()
        time.sleep(2)
        print("success click to random product category")
        # test click to random product category
        elem = driver.find_elements_by_css_selector('div.Select-menu-outer')
        # create a list and chose a random product category
        bnd = elem[randint(0, len(elem) - 1)]
        bnd.click()
        time.sleep(2)
        print("success click to choose product category")
        # test click to random sub product category
        print("Product Sub Category")
        elem = driver.find_elements_by_css_selector('div.Select-control')
        # create a list and chose a random product category
        ds = elem[randint(0, len(elem) - 1)]
        ds.click()
        time.sleep(2)
        print("success click to random product category")
        # test click to random product category
        elem = driver.find_elements_by_css_selector('div.Select-menu-outer')
        # create a list and chose a random product category
        bnd = elem[randint(0, len(elem) - 1)]
        bnd.click()
        time.sleep(2)
        print("success click to choose product category")
        # test for product name
        print("Product Name")
        elem = driver.find_element_by_xpath("//input[@placeholder='Enter Product Name (Do Not Include Brand Name)']")
        elem.send_keys("Concealer")
        time.sleep(2)
        print("success enter product name")
        # test for product shade / variant name
        print("Product Shade / Variant Name")
        elem = driver.find_element_by_xpath("//input[@placeholder='Type in The Shade / Variant Name (If Any Available)']")
        elem.send_keys("Sand")
        time.sleep(2)
        print("success enter product shade / variant name")
        driver.execute_script("window.scrollBy(0,200);")
        time.sleep(2)
        # test for click next
        print("Next")
        elem = driver.find_element_by_xpath("//input[@value='NEXT']")
        elem.click()
        time.sleep(2)
        print("success click next")

        # START TO UPLOAD PRODUCT RATING
        print("START TO UPLOAD PRODUCT RATING")
        # test for product rating
        driver.execute_script("window.scrollBy(0,-210);")
        time.sleep(2)
        elem = driver.find_elements_by_css_selector('div.ar-starlist')
        # create a list and chose a random star
        sl = elem[randint(0, len(elem) - 1)]
        sl.click()
        time.sleep(2)
        print("success click to choose random rating")
        # test click to random a random type of filter
        elem = driver.find_elements_by_css_selector('i.ar-star-grey')
        # create a list and chose a random type of filter
        sg = elem[randint(0, len(elem) - 1)]
        sg.click()
        time.sleep(2)
        print("success click to choose star")
        # RANDOM PRODUCT PRICE
        print("RANDOM PRODUCT PRICE")
        # test filter reviews
        elem = driver.find_elements_by_css_selector('div.ar-btn-txt')
        # create a list and chose a random filter review
        pp = elem[randint(0, len(elem) - 1)]
        pp.click()
        time.sleep(2)
        print("success click to choose random product price")
        # test click to random a random type of filter
        elem = driver.find_elements_by_css_selector('button.right')
        # create a list and chose a random type of filter
        ppb = elem[randint(0, len(elem) - 1)]
        ppb.click()
        time.sleep(2)
        print("success click to choose product price")
        # RANDOM PACKAGE QUALITY
        print("RANDOM PACKAGE QUALITY")
        # test filter reviews
        elem = driver.find_elements_by_css_selector('div.ar-btn-txt')
        # create a list and chose a random filter review
        pq = elem[randint(0, len(elem) - 1)]
        pq.click()
        time.sleep(2)
        print("success click to choose random package quality")
        # test click to random a random type of filter
        elem = driver.find_elements_by_css_selector('button.right')
        # create a list and chose a random type of filter
        pqb = elem[randint(0, len(elem) - 1)]
        pqb.click()
        time.sleep(2)
        print("success click to choose package quality")
        # RANDOM REPURCHASE
        print("RANDOM REPURCHASE")
        # test filter reviews
        elem = driver.find_elements_by_css_selector('div.ar-btn-txt')
        # create a list and chose a random filter review
        rr = elem[randint(0, len(elem) - 1)]
        rr.click()
        time.sleep(2)
        print("success click to choose random repurchase")
        # test click to random a random type of filter
        elem = driver.find_elements_by_css_selector('button.right')
        # create a list and chose a random type of filter
        rrb = elem[randint(0, len(elem) - 1)]
        rrb.click()
        time.sleep(2)
        print("success click to choose repurchase")
        # test typing review
        elem = driver.find_element_by_xpath(
            "//textarea[@placeholder='Add your review (at least 200 characters long). Tip : A good review includes your experience while using the product. wether it was effective or not. how long did it last. etc.']")
        elem.click()
        elem.send_keys(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
        time.sleep(2)
        print("success input review product")
        driver.execute_script("window.scrollBy(0,200);")
        time.sleep(2)
        # test for click next
        print("Next")
        elem = driver.find_element_by_xpath("//input[@value='NEXT']")
        elem.click()
        time.sleep(2)
        print("success click next")

        # START TO UPLOAD PRODUCT INFO
        print("START TO UPLOAD PRODUCT INFO")
        # test for product info
        driver.execute_script("window.scrollBy(0,-200);")
        time.sleep(2)
        elem = driver.find_elements_by_css_selector('div.Select-value')
        # create a list and choose a random currency
        sl = elem[randint(0, len(elem) - 1)]
        sl.click()
        time.sleep(2)
        print("success click to choose random rating")
        # test click to random a random type of filter
        elem = driver.find_elements_by_css_selector('span.Select-value-label')
        # create a list and chose a random type of filter
        sg = elem[randint(0, len(elem) - 1)]
        sg.click()
        time.sleep(2)
        print("success click to choose star")
        # test input currency
        elem = driver.find_element(By.XPATH, '//input[placeholder()="ex 10000"]')
        elem.send_keys("250000")
        time.sleep(2)
        print("success input currency")
        # test add product description
        elem = driver.find_element_by_xpath("//textarea[@placeholder='Add product information like uses, benefits, etc.']")
        elem.click()
        elem.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
        time.sleep(2)
        print("success input add product description")
        # test product tags
        # test for click submit
        elem = driver.find_element(By.XPATH, '//input[value()="SUBMIT"]')
        elem.click()
        time.sleep(2)
        print("success click submit")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
