import time

import pytest
from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from frameworkPractc.baseclassone import BaseClassOne
from frameworkPractc.topPage import topPages
from pytestDemo.BaseClass import BaseClass



class TestprctcPages:

    @pytest.fixture()
    def setup(self):
        service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_obj)
        self.driver.implicitly_wait(4)



    def test_topPages(self, setup):
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        self.driver.maximize_window()
        toppage = topPages(self.driver)
        toppage.getRadiobtn().click()
        #radioButtons = self.driver.find_elements(By.CSS_SELECTOR, ".radioButton")
        #radioButtons[1].click()

        suggestionsPage = topPages(self. driver)
        suggestionsPage.getSuggestions().send_keys("Ind")
        #self.driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys("Ind")
        countries = self.driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] div")

        for country in countries:
            if country.text == "India":
                country.click()
                break

        dropDown = topPages(self. driver)
        dropDown.getDropdown().select_by_value("option2")
        #dropdown = Select(self.driver.find_element(By.CSS_SELECTOR,"#dropdown-class-example"))
        #dropdown.select_by_value("option2")
        #dropdown.select_by_value("option2")
        checkboxes = topPages(self. driver)
        checkboxes.getCheckbox().click()
        #self.driver.find_element(By.CSS_SELECTOR,"#checkBoxOption2").click()

    def test_mousehover(self, setup):
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()
        action.move_to_element(self.driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

    def test_childwindow(self, setup):
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        self.driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
        windowsOpened = self.driver.window_handles
        self.driver.switch_to.window(windowsOpened[1])
        print(self.driver.find_element(By.XPATH,"//h1[normalize-space()='Documents request']").text)
        self.driver.switch_to.window(windowsOpened[0])
        self.driver.find_element(By.CSS_SELECTOR,"#username").send_keys("Imran")
        self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys("imran1996")
        self.driver.find_element(By.XPATH,"(//span[@class='checkmark'])[1]").click()
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR,"select[class='form-control']"))
        dropdown.select_by_visible_text("Teacher")
        self.driver.find_element(By.CSS_SELECTOR,"#terms").click()
        self.driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()









        time.sleep(5)