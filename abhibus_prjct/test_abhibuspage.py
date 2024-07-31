import time
import time

import pytest
from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys, log
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from abhibus_prjct.BaseClass import Baseclass
from abhibus_prjct.allPages import allabhibus
from abhibus_prjct import BaseClass

@pytest.mark.usefixtures("setup")
class TestAbhiBus(Baseclass):

    def test_abhiBus(self, setup):
        log = self.getLogger()
        allpages = allabhibus(self. driver)
        log.info("These are Origin starting details")
        allpages.getFromLoc().send_keys("Hyderabad", Keys.ENTER)
        log.info("These are destination reaching details")
        allpages.getToLoc().send_keys("Bangalore", Keys.ENTER)
        allpages.getDate().click()
        #driver.find_element(By.XPATH, "//input[@placeholder='From Station']").send_keys("Hyderabad", Keys.ENTER)
        #driver.find_element(By.XPATH, "//input[@placeholder='To Station']").send_keys("Bangalore", Keys.ENTER)
        #driver.find_element(By.XPATH, "//div/button[text()='Tomorrow']").click()
        time.sleep(5)
        log.debug("These are filters used")
        allpages.getFilterOne().click()
        allpages.getFilterTwo().click()
        log.info("This is bus type")
        allpages.getBusType().click()
        #driver.find_element(By.XPATH, "//div[contains(@class,'row filter-wrapper')]//a[1]").click()
        #driver.find_element(By.CSS_SELECTOR, "#price-drop").click()
        #driver.find_element(By.XPATH,"//div/img[@src='https://static.abhibus.com/offerbanners/Jun2024/26/1719399172/streamlinebus.webp']").click()
        self.driver.implicitly_wait(5)
        allpages.getSeat().click()
        #driver.find_element(By.XPATH, "//button[text()='Show Seats']").click()
        time.sleep(5)
        log.info("This is seat selection details")
        allpages.getSeatSelect().click()
        log.info("Theses are boarding point details")
        allpages.getBoardingPoint().send_keys("k")
        allpages.getBoardingPointOne().click()
        log.info("These are dropping point details")
        allpages.getDroppingPoint().send_keys("silk")
        allpages.getDroppingPointOne().click()
        #driver.find_element(By.XPATH,"//table[@id='seat-layout-details'][1]/tbody/tr[2]/td[3]/div/button/span[text()='C1']").click()
        #driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Boarding Point']").send_keys("K")
        #driver.find_element(By.XPATH, "//div/p[text()='Kondapur (Pickup Van/Bus)']").click()
        #driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Dropping Point']").send_keys("silk")
        #driver.find_element(By.XPATH, "//div/p[text()='Silk Board']").click()

        self.driver.execute_script("window.scrollBy(0,500);")
        log.info("This is selecting seat details")
        allpages.getSelectSeat().click()
        #driver.find_element(By.XPATH, "//div[text()='Selected Seat']").click()

        # bus_stop = driver.find_elements(By.CSS_SELECTOR,"#place-container")

        # for stop in bus_stop:
        #   if stop.text == "Kondapur":
        #      stop.click()

        time.sleep(5)
