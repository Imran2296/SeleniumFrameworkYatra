import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.find_element(By.CSS_SELECTOR,"div[aria-label='Close']").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")


time.sleep(5)