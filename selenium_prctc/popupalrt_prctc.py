import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
name = "imran"
service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertTxt = alert.text
print(alertTxt)
alert.accept()
#alert.dismiss can be used to cancel and alert.accept can be used as 'ok'
assert name in alertTxt

time.sleep(5)