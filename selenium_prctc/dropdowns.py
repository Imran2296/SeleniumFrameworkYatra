import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(4)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")


for country in countries:
    if country.text() == "India":
        country.click()
        break

print(driver.find_element(By.ID,"autosuggest").text)
