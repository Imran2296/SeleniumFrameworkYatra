import time
import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(4)
countriesnew = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")

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

driver.find_element(By.ID,"ctl00_mainContent_rbtnl_Trip_1").click()

time.sleep(4)
driver.find_element(By.ID,"ctl00_mainContent_ddl_originStation1").send_keys("DEL")
#dropdown.select_by_index(4)

toDropdown = Select(driver.find_element(By.NAME,"ctl00$mainContent$ddl_destinationStation1"))
toDropdown.select_by_value("BLR")