import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

dropdown = Select(driver.find_element(By.ID,"dropdown-class-example"))
dropdown.s


time.sleep(5)