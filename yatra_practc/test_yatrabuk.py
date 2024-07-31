import time

from select import select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from yatra_practc.allPages import AllPages


class TestYatraBuk:

    def test_yatrabuks(self, setup):
        allInOnePage = AllPages(self.driver)
        time.sleep(3)
        allInOnePage.getFromPlace().click()
        time.sleep(2)
        allInOnePage.getFromPlace().send_keys("Hyd")
        time.sleep(2)
        allInOnePage.getFromPlace().send_keys(Keys.ENTER)
        #departFrom = driver.find_element(By.XPATH, "//input[@name='flight_origin' and @id='BE_flight_origin_city']")
        #departFrom.click()
        #time.sleep(3)
        #departFrom.send_keys("Hyd")
        #time.sleep(2)
        #departFrom.send_keys(Keys.ENTER)
        #to_Place = AllPages(self. driver)
        allInOnePage.getToPlace().click()
        time.sleep(2)
        allInOnePage.getToPlace().send_keys("Banga")
        time.sleep(2)
        allInOnePage.getToPlace().send_keys(Keys.ENTER)
        time.sleep(3)
        #goingTo = driver.find_element(By.XPATH, "//input[@name='flight_destination' and @id='BE_flight_arrival_city']")
        #goingTo.click()
        #time.sleep(2)
        #goingTo.send_keys("banga")
        #time.sleep(2)
        #goingTo.send_keys(Keys.ENTER)

        # driver.find_element(By.XPATH,"//a[@title='Round Trip']").click()
        #goingDate = AllPages(self.driver)
        allInOnePage.getOriginiDate().click()
        allInOnePage.getSelectOriginDate().click()
        #driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
        #driver.find_element(By.XPATH, "//td[@data-date='06/08/2024']").click()
        #studentFare = AllPages(self. driver)
        allInOnePage.getStudentFare().click()
        allInOnePage.getNonStopFlight().click()

        #driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']").click()
        #driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").click()
        self.driver.execute_script("window.scrollBy(0,300)")
        allInOnePage.getSearchFlight().click()
        allInOnePage.getBookFlight().click()
        #driver.find_element(By.XPATH, "//input[@type='submit' and @value='Search Flights']").click()
        #driver.find_element(By.XPATH, "(//button[@class='fs-14 secondary-button select-button button border-thin cursor-pointer bold'][normalize-space()='Book Now'])[1]").click()
        # driver.find_element(By.XPATH,"//a[@title='Round Trip']").click()

        time.sleep(6)