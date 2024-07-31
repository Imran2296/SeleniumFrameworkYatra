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
time.sleep(5)
driver.get("file:///C:/Users/191485/Desktop/imranloginpage.html")
driver.find_element(By.ID,"username").send_keys("imransk")
driver.find_element(By.ID,"password").send_keys("immu1996")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(5)