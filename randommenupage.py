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

        # test login an account
        print("Login Account")
        elem = driver.find_element_by_xpath("//div[@class='jsx-3923003960 gbheader-login']")
        elem.click()
        time.sleep(2)
        print("success click login/signup")
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
        # test smooth scrolling up through the page
        driver.execute_script("window.scrollBy(0,-200);")
        time.sleep(2)
        print("success smooth scrolling through the page")

        # test random menu bar
        print("Random Menu Bar")
        # test click to random menu bar for menu bar
        elem = driver.find_elements_by_css_selector('div.gtmenu-menu-text')
        # create a list and chose a random menu bar
        menubar = elem[randint(0, len(elem) - 1)]
        menubar.click()
        time.sleep(2)
        print("success click to random menu bar")
        driver.execute_script("window.scrollBy(0,200);")
        time.sleep(2)
        print("success smooth scrolling through the page")

        # # RANDOM FILTER BY CATEGORY
        # print("RANDOM FILTER BY CATEGORY")
        # # test click to random filter by category
        # elem = driver.find_elements_by_css_selector('a.jsx-17482050 filter-category-desktop-category')
        # # create a list and chose a random filter by category
        # fbc = elem[randint(0, len(elem) - 1)]
        # fbc.click()
        # time.sleep(5)
        # print("setup click to random filter by category")
        # driver.execute_script("window.scrollBy(0,200);")
        # time.sleep(2)
        # print("setup smooth scrolling through the page")
        #
        # # RANDOM FILTER BY BRANDS
        # print("RANDOM FILTER BY BRANDS")
        # # test click to random filter by brands
        # elem = driver.find_elements_by_css_selector('a.jsx-17482050 filter-category-desktop-category')
        # # create a list and chose a random filter by brands
        # fbb = elem[randint(0, len(elem) - 1)]
        # fbb.click()
        # time.sleep(5)
        # print("setup click to random filter by brands")
        # driver.execute_script("window.scrollBy(0,200);")
        # time.sleep(2)
        # print("setup smooth scrolling through the page")

        # testing menu category product
        print("Testing Menu Category Product")
        # test click to menu category product for choose by category popular
        elem = driver.find_element(By.XPATH, '//button[text()="popular"]')
        elem.click()
        time.sleep(2)
        print("success click to menu category product for choose by category popular")
        # test click to menu category product for choose by category newest
        elem = driver.find_element(By.XPATH, '//a[text()="newest"]')
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//button[text()="newest"]')
        elem.click()
        time.sleep(2)
        print("success click to menu category product for choose by category newest")
        # test click to menu category product for choose by category highprice
        elem = driver.find_element(By.XPATH, '//a[text()="highestprice"]')
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//button[text()="highestprice"]')
        elem.click()
        time.sleep(2)
        print("success click to menu category product for choose by category highestprice")
        # test click to menu category product for choose by category lowprice
        elem = driver.find_element(By.XPATH, '//a[text()="lowprice"]')
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//button[text()="lowprice"]')
        elem.click()
        time.sleep(2)
        print("success click to menu category product for choose by category lowprice")
        # test click to menu category product for choose by category highrating
        elem = driver.find_element(By.XPATH, '//a[text()="highrating"]')
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//button[text()="highrating"]')
        elem.click()
        time.sleep(2)
        print("success click to menu category product for choose by category highrating")
        # test click to menu category product for choose by category lowrating
        elem = driver.find_element(By.XPATH, '//a[text()="lowrating"]')
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//button[text()="lowrating"]')
        elem.click()
        time.sleep(2)
        print("success click to menu category product for choose by category lowrating")
        # test click to menu category product for choose by category popular
        elem = driver.find_element(By.XPATH, '//a[text()="popular"]')
        elem.click()
        time.sleep(2)
        print("success click to menu category product for choose by category popular")

        # test click random product
        print("Random Product")
        # test click to random product for add reviews of products
        elem = driver.find_elements_by_css_selector('div.productcardnew-product')
        # create a list and chose a random of products
        product = elem[randint(0, len(elem) - 1)]
        product.click()
        time.sleep(2)
        print("success click to random product for add reviews of products")
        driver.execute_script("window.scrollBy(0,-200);")
        time.sleep(2)
        print("success smooth scrolling the page")

        # test random overall rating
        print("Random Overall Rating")
        # test filter reviews
        elem = driver.find_elements_by_css_selector('div.ar-starlist')
        # create a list and chose a random filter review
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
        # test random product price
        print("Random Product Price")
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
        # test click random package quality
        print("Random Package Quality")
        # test filter reviews
        elem = driver.find_elements_by_css_selector('div.ar-btn-txt')
        # create a list and chose a random filter review
        pq = elem[randint(0, len(elem) - 1)]
        pq.click()
        time.sleep(2)
        print("success click to choose random product price")
        # test click to random a random type of filter
        elem = driver.find_elements_by_css_selector('button.right')
        # create a list and chose a random type of filter
        pqb = elem[randint(0, len(elem) - 1)]
        pqb.click()
        time.sleep(2)
        print("success click to choose product price")
        # test click random repurchase
        print("Random Repurchase")
        # test filter reviews
        elem = driver.find_elements_by_css_selector('div.ar-btn-txt')
        # create a list and chose a random filter review
        rr = elem[randint(0, len(elem) - 1)]
        rr.click()
        time.sleep(2)
        print("success click to choose random product price")
        # test click to random a random type of filter
        elem = driver.find_elements_by_css_selector('button.right')
        # create a list and chose a random type of filter
        rrb = elem[randint(0, len(elem) - 1)]
        rrb.click()
        time.sleep(2)
        print("success click to choose product price")
        # # test click to submit review for add reviews of products
        # elem = driver.find_element_by_xpath("//input[@value='SUBMIT REVIEW']")
        # elem.click()
        # time.sleep(2)
        # print("test click to submit review for add reviews of products")

        # test click to product
        print("Product Review")
        elem = driver.find_element_by_xpath("//div[@class='productcardnew-titleprod']")
        elem.click()
        time.sleep(2)
        print("success click to choose product")
        # test smooth scrolling through the page
        driver.execute_script("window.scrollBy(0,400);")
        time.sleep(2)
        print("success smooth scrolling through the page")
        # test click to wishlist for reviews of products
        elem = driver.find_element(By.XPATH, '//button[text()="wishlist"]')
        elem.click()
        time.sleep(2)
        print("success click to wishlist for one product")
        # test click to tried it for reviews of products
        elem = driver.find_element(By.XPATH, '//button[text()="tried it"]')
        elem.click()
        time.sleep(2)
        print("success click to tried it for reviews of products")

        # test smooth scrolling through the page
        driver.execute_script("window.scrollBy(0,400);")
        time.sleep(2)
        print("success smooth scrolling through the page")
        # test click tab bar info, the brand, articles, post
        elem = driver.find_element(By.XPATH, '//a[text()="info"]')
        elem.click()
        time.sleep(2)
        print("success click tab bar info")
        elem = driver.find_element(By.XPATH, '//a[text()="the brand"]')
        elem.click()
        time.sleep(2)
        print("success click tab bar the brand")
        elem = driver.find_element(By.XPATH, '//a[text()="articles"]')
        elem.click()
        time.sleep(2)
        print("success click tab bar articles")
        elem = driver.find_element(By.XPATH, '//a[text()="post"]')
        elem.click()
        time.sleep(2)
        print("success click tab bar post")
        elem = driver.find_element(By.XPATH, '//a[text()="reviews"]')
        elem.click()
        time.sleep(2)
        print("success click tab bar reviews")
        driver.execute_script("window.scrollBy(0,400);")
        time.sleep(2)
        print("success smooth scrolling the page")

        # test reviews by filter
        print("Reviews By Filter")
        # test filter reviews
        elem = driver.find_elements_by_css_selector('button.dropbtn')
        # create a list and chose a random filter review
        fr = elem[randint(0, len(elem) - 1)]
        fr.click()
        time.sleep(2)
        print("success click to choose random filter")
        # test click to random a random type of filter
        elem = driver.find_elements_by_css_selector('div.jsx-3197642051 dropdown-content')
        # create a list and chose a random type of filter
        ds = elem[randint(0, len(elem) - 1)]
        ds.click()
        time.sleep(2)
        print("success click to random type of filter")

        # # test click to like or love for reviews of products
        # elem = driver.find_element(By.XPATH, '//a[text()=" Like"]')
        # elem.click()
        # time.sleep(2)
        # print("setup click to like or love for reviews of products")
        # # test click to like or love for reviews of products
        # elem = driver.find_element(By.XPATH, '//a[text()=" Like"]')
        # elem.click()
        # time.sleep(2)
        # print("setup click to like or love for reviews of products")
        # # test click to edit reviews of products
        # elem = driver.find_element(By.XPATH, '//a[text()="Edit"]')
        # elem.click()
        # time.sleep(4)
        # print("setup click to edit reviews of products")
        # # test click to cancel for edit reviews of products
        # elem = driver.find_element(By.XPATH, '//span[text()="CANCEL"]')
        # elem.click()
        # time.sleep(4)
        # print("setup click to cancel for edit reviews of products")

        # # test to open review for add comment
        # driver.execute_script("window.scrollBy(0,200);")
        # time.sleep(2)
        # elem = driver.find_element(By.XPATH, '//div[class()="card-review-new-coment"]')
        # elem.click()
        # # test comment
        # elem = driver.find_element_by_xpath(
        #     "//textarea[@placeholder='Add your review (at least 200 characters long). Tip : A good review includes your experience while using the product. wether it was effective or not. how long did it last. etc.']")
        # elem.click()
        # elem.send_keys(
        #     "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
        # time.sleep(2)
        # print("setup add review ")
        # # test click post comment
        # elem = driver.find_element_by_css_selector("input.addcomment-btn-post")
        # elem.click()
        # time.sleep(2)
        # print("setup add comment")
        # # test click close
        # elem = driver.find_element_by_xpath(
        #     "//img[contains(@src, '/static/images/ic_close_dark_grey.png')]/parent::div")
        # elem.click()
        # time.sleep(2)
        # print("setup click close")
        #
        # # test smooth scrolling through the page
        # driver.execute_script("window.scrollBy(0,-1600);")
        # time.sleep(2)
        # print("setup smooth scrolling the page")

        # test logout account
        elem = driver.find_element_by_xpath("//span[@class='gbheader-username']")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        time.sleep(2)
        print("setup click header user profile")
        elem = driver.find_element(By.XPATH, '//a[text()="Logout"]')
        elem.click()
        time.sleep(5)
        print("setup click logout")
        driver.execute_script("window.scrollBy(0,-200);")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-200);")
        time.sleep(2)
        print("setup smooth scrolling the page")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
