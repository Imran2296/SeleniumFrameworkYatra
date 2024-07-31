import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"(//input[@name='name'])[1]").send_keys("Rahul")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("shetty")
driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys("imran")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()

#static dropdown(we need to use 'select')
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
#dropdown.select_by_index(0)
dropdown.select_by_visible_text("Male")
time.sleep(4)
driver.find_element(By.XPATH,"//input[@value='Submit']").click()

alertText = driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text

assert("Success" in alertText)