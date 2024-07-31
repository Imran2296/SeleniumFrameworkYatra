import time

import pytest
from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from frameworkpractctwo.BaseClass import Baseclass
from frameworkpractctwo.CountryPage import CountryPage
from frameworkpractctwo.KartPage import KartPage
from frameworkpractctwo.MainPage import MainPage
from frameworkpractctwo.PlaceOrderPage import PlaceOrder


@pytest.mark.usefixtures("setup")
class TestGreenKart(Baseclass): #Baseclass is the class used for logging


    def test_greenKart(self, setup):
        log = self.getLogger() #used for logging
        searchPage = MainPage(self.driver)
        log.info("Entering vegetables names that starts with be")
        searchPage.getSearch().send_keys("be")
        #self.driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
        time.sleep(2)  # even though we have implicit wait, we r having sleep her coz of 'driver.find_elements'
        results = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")  # list of web elements
        count = len(results)
        assert count > 0
        for result in results:
            result.find_element(By.XPATH, "div/button").click()

        cart = self.driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']")
        cart.click()
        log.info("Details of kart page")
        kartpage = KartPage(self.driver)
        kartpage.getKartPage().click()
        #self.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
        placeorder = PlaceOrder(self. driver)
        placeorder.getPromocode().send_keys("rahulshettyacademy")
        #self.driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
        placeorder.getApplycode().click()
        #self.driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
        total_amount = int(self.driver.find_element(By.CSS_SELECTOR,".totAmt").text)
        afterDiscount_amount = float(self.driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

        assert total_amount > afterDiscount_amount
        placeorder.getOrderplace().click()

        #self.driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

        countrypage = CountryPage(self.driver)
        countrypage.getCountry().select_by_value("India")

        #dropdown = Select(self.driver.find_element(By.XPATH, "(//select)[1]"))
        #dropdown.select_by_value("India")

        countrypage.getCheckbox().click()
        countrypage.getSubmit().click()

        #self.driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
        #self.driver.find_element(By.XPATH, "//button[text()='Proceed']").click()



        time.sleep(5)

        #write another testcase for booking flights which is in the same url

    def test_Flightbook(self, setup):

        self.driver.find_element(By.XPATH,"//a[normalize-space()='Flight Booking']").click()
        windowsopened = self.driver.window_handles
        self.driver.switch_to.window(windowsopened[1])
        time.sleep(5)
        self.driver.find_element(By.ID, "autosuggest").send_keys("Ind")
        time.sleep(4)
        countriesnew = self.driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")

        for country in countriesnew:
            if country.text == "India":
                country.click()
                break
        #self.driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("Ind")
        #countrynew = self.driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")

        #for country in countrynew:
            #if country.text == 'India':
                #country.click()
                #break

        self.driver.find_element(By.ID,"ctl00_mainContent_rbtnl_Trip_1").click()

        #fromdropdown = Select(self.driver.find_element(By.XPATH,"//select[@id='ctl00_mainContent_ddl_originStation1']"))
        #fromdropdown.select_by_value("DEL")

        #toDropdown = Select(self.driver.find_element(By.NAME,"ctl00$mainContent$ddl_destinationStation1"))
        #toDropdown.select_by_value("BLR")

        #self.driver.find_element(By.CSS_SELECTOR,"#ui-state-default.ui-state-highlight.ui-state-active").click()
        #self.driver.find_element(By.XPATH,"//a[normalize-space()='24']").click()

        currencyDropdown = Select(self.driver.find_element(By.CSS_SELECTOR,"#ctl00_mainContent_DropDownListCurrency"))
        currencyDropdown.select_by_visible_text("AED")

        self.driver.find_element(By.XPATH,"//input[@id='ctl00_mainContent_chk_StudentDiscount']").click()

        self.driver.find_element(By.CSS_SELECTOR,"#ctl00_mainContent_btn_FindFlights").click()

        print("Enter From and To details")

        time.sleep(5)







