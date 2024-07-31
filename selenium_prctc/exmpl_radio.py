import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


radiobtn = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobtn[2].click()
# .radioButton
# #radioButton
# input[name='radioButton']


time.sleep(4)