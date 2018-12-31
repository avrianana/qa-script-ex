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
        driver.get("http://femaledaily.net/")
        driver.set_page_load_timeout(2)
        driver.maximize_window()
        # driver.set_window_size(1341, 810)
        driver.implicitly_wait(2)
        time.sleep(2)
        print("success open website femaledaily.net")

        # test login an account
        print("Login Account")
        elem = driver.find_element_by_xpath("//div[@class='jsx-1624868303 gbheader-login']")
        elem.click()
        time.sleep(2)
        print("success click login/signup")
        # test click username and password
        print("Username and Account")
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

        # test click bar profile
        print("Bar Profile")
        elem = driver.find_element_by_xpath("//div[@class='gbheader-userprofile']")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        time.sleep(2)
        print("success click bar user profile")
        # test click unread notification
        print("Unread Notification")
        elem = driver.find_element_by_class_name("gbheader-unread-notif")
        elem.click()
        time.sleep(3)
        print("success click Unread Notification")
        # test click breadcrumbs
        print("Breadcrumbs")
        elem = driver.find_element_by_xpath("//a[@class='jsx-2093859422 breadcrumb-section']")
        elem.click()
        time.sleep(2)
        print("success click breadcrumbs home")

        # test click bar profile
        print("Bar Profile")
        elem = driver.find_element_by_xpath("//div[@class='gbheader-userprofile']")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        time.sleep(2)
        print("success click bar user profile")
        # test click feed
        print("Feed")
        elem = driver.find_element_by_xpath("//a[@href='/user/putwid/feeds']")
        elem.click()
        time.sleep(3)
        print("success click feed")
        # # test smooth scrolling through the page
        # driver.execute_script("window.scrollBy(0,300);")
        # time.sleep(5)
        # print("success smooth scrolling through the page")
        # # test click random read more
        # print("Read More")
        # elem = driver.find_element_by_xpath("//div[@class='jsx-3694137456 feed-review-readmore']")
        # elem.click()
        # time.sleep(6)
        # print("success click read more")

        # test click bar profile
        print("Bar Profile")
        elem = driver.find_element_by_xpath("//div[@class='gbheader-userprofile']")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        time.sleep(2)
        print("success click bar user profile")
        # test click my profile
        print("My Profile")
        elem = driver.find_element_by_xpath("//a[@href='/user/putwid?tab=posts']")
        elem.click()
        time.sleep(3)
        print("success click my profile")
        # test smooth scrolling through the page
        driver.execute_script("window.scrollBy(0,1800);")
        time.sleep(2)
        print("success smooth scrolling through the page")
        # test click badges&beauty id
        print("Badges & Beauty ID")
        elem = driver.find_element(By.XPATH, '//a[text()="badges & beauty id"]')
        elem.click()
        time.sleep(2)
        print("success click badges&beauty id")
        # test click next on badges
        elem = driver.find_element_by_xpath("//div[@class='jsx-2938039691 badges-btn-next']")
        elem.click()
        time.sleep(2)
        print("success click next on badges")
        # test click prev on badges
        elem = driver.find_element_by_xpath("//div[@class='jsx-2938039691 badges-btn-prev']")
        elem.click()
        time.sleep(2)
        print("success click prev on badges")
        # elem = driver.find_element_by_xpath("//div[@class='jsx-2938039691 badges-earn']")
        # elem.click()
        # time.sleep(2)
        # print("success click how to earn")
        # test click wishlist
        print("Wishlist")
        elem = driver.find_element(By.XPATH, '//a[text()="wishlist"]')
        elem.click()
        time.sleep(10)
        print("success click wishlist")
        # test click product tried
        print("Product Tried")
        elem = driver.find_element(By.XPATH, '//a[text()="products tried"]')
        elem.click()
        time.sleep(10)
        print("success click product tried")

        # test check followers
        print("Followers")
        elem = driver.find_element(By.XPATH, '//div[text()="followers"]')
        elem.click()
        time.sleep(2)
        print("success click followers")
        # test smooth scrolling up through the page
        driver.execute_script("window.scrollBy(0,200);")
        time.sleep(2)

        # test check following
        print("Following")
        elem = driver.find_element(By.XPATH, '//div[text()="following"]')
        elem.click()
        time.sleep(5)
        print("success click following")
        # test smooth scrolling up through the page
        # driver.execute_script("window.scrollBy(0,400);")
        # time.sleep(2)

        # test check reviews
        print("Reviews")
        elem = driver.find_element(By.XPATH, '//div[text()="reviews"]')
        elem.click()
        time.sleep(5)
        print("success click reviews")
        # test smooth scrolling up through the page
        # driver.execute_script("window.scrollBy(0,400);")
        # time.sleep(2)

        # test check posts
        print("Posts")
        elem = driver.find_element(By.XPATH, '//div[text()="posts"]')
        elem.click()
        time.sleep(5)
        print("success click posts")
        # test smooth scrolling up through the page
        # driver.execute_script("window.scrollBy(0,400);")
        # time.sleep(2)

        # test check points
        print("Points")
        elem = driver.find_element(By.XPATH, '//div[text()="points"]')
        elem.click()
        time.sleep(5)
        print("success click points")
        # test smooth scrolling up through the page
        driver.execute_script("window.scrollBy(0,400);")
        time.sleep(2)
        # test click what is point & how i can earn point
        print("What Is Point & How I Can Earn Point")
        elem = driver.find_element(By.XPATH, '//a[href()="/help"]')
        elem.click()
        time.sleep(5)
        print("success click points")
        driver.execute_script("window.scrollBy(0,-400);")
        time.sleep(2)
        print("success smooth scrolling through the page")

        # test click settings button
        print("Settings Button")
        elem = driver.find_element(By.XPATH, '//button[text()="settings"]')
        elem.click()
        time.sleep(5)
        print("success click settings button")

        # test click bar profile
        print("Bar Profile")
        elem = driver.find_element_by_xpath("//div[@class='gbheader-userprofile']")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        time.sleep(2)
        print("success click bar user profile")
        # test click settings on bar user profile
        print("Settings Bar")
        elem = driver.find_element_by_xpath("//a[@href='/my/account?tab=account_information']")
        elem.click()
        time.sleep(3)
        print("success click settings bar")

        # test click logout
        print("Logout")
        elem = driver.find_element_by_xpath("//span[@class='gbheader-username']")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        time.sleep(2)
        print("setup click header user profile")
        elem = driver.find_element(By.XPATH, '//a[text()="Logout"]')
        elem.click()
        time.sleep(3)
        print("setup click logout")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
