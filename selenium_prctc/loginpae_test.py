import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//input[@id='userPassword']").send_keys("imrran123")
driver.find_element(By.XPATH,"//input[@id='confirmPassword']").send_keys("imrran123")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()





time.sleep(6)