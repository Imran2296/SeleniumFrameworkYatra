import time
import time

import pytest
from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from framewrkprctcthree.Baseclass import Baseclass
from framewrkprctcthree.GroceriesPage import groceriesPage
from framewrkprctcthree.detailsPage import DetailsPage
from framewrkprctcthree.mobilepage import MobilePage
#MOBILE PHONE
@pytest.mark.usefixtures("setup")
class TestFlipKart(Baseclass):

    def test_flipkart(self, setup):
        log = self.getLogger()
        mobilePage = MobilePage(self.driver)
        log.info("Mobile page")
        mobilePage.getMobilePage().click()
        mobilePage.getAlliphones().click()
        log.debug("This is iphone 14 plus blue colour")
        mobilePage.getIphone().click()
        #driver.find_element(By.CSS_SELECTOR, "img[alt='Mobiles']").click()
        #driver.find_element(By.XPATH, "//div[@class='X8l5DD']//div[1]//a[1]//div[1]//img[2]").click()
        #driver.find_element(By.XPATH, "//div[normalize-space()='Apple iPhone 14 Plus (Blue, 128 GB)']").click()

        windowopen = self.driver.window_handles
        self.driver.switch_to.window(windowopen[1])
        #self.driver.execute_script("window.scrollBy(0,600);")
        self.driver.implicitly_wait(5)

        detailsPage = DetailsPage(self. driver)
        detailsPage.getPincode().send_keys("520001")
        detailsPage.getConfrmpincode().click()
        log.info("A memory of 256 gb")
        detailsPage.getMemory().click()
        self.driver.implicitly_wait(4)
        #driver.find_element(By.CSS_SELECTOR, "#pincodeInputId").send_keys("520001")
        #driver.find_element(By.CSS_SELECTOR, ".i40dM4").click()
        #driver.find_element(By.XPATH, "//a[text()='512 GB']").click()
        self.driver.execute_script("window.scrollBy(0,600);")
        detailsPage.getCart().click()
        self.driver.implicitly_wait(4)
        #driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
        #GROCERIES
        log.info("This is groceries page")
        groceryPages = groceriesPage(self.driver)
        self.driver.execute_script("window.scrollBy(0,100);")
        groceryPages.getPage().click()
        groceryPages.getSearch().click()
        #self.driver.find_element(By.CSS_SELECTOR, "div[class='IFZV3u']").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".QqFHMw.aEsfVh.M5XAsp").click()
        self.driver.implicitly_wait(5)
        groceryPages.getGhee().send_keys("ghee")
        log.info("Search for ghee if you want ghee")
        groceryPages.getSearchsubmit().click()
        groceryPages.getGheepage().click()
        #self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search grocery products']").send_keys("ghee")
        #self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        #self.driver.find_element(By.XPATH, "//img[@alt='Godrej Jersey Pure Cow Ghee 1 L Pouch (Neyyi)']").click()

        windowopened = self.driver.window_handles
        self.driver.switch_to.window(windowopened[2])
        self.driver.execute_script("window.scrollBy(0,900);")
        groceryPages.getSubmitghee().click()
        #self.driver.find_element(By.CSS_SELECTOR, "button[class='QqFHMw vslbG+ In9uk2 pKi72Z']").click()
        time.sleep(5)
        log.info("You will have iphone and ghee in your cart")
        groceryPages.getFinalcart().click()
        #self.driver.find_element(By.CSS_SELECTOR, "._9Wy27C").click()

        time.sleep(5)
