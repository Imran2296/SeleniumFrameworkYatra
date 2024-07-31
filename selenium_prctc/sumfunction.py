#explicit wait: here we can target to one particular element,
# you can set explicitely to that particular element upto given secs (15 secs)

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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2) #even though we have implicit wait, we r having sleep her coz of 'driver.find_elements'
results = driver.find_elements(By.XPATH,"//div[@class='products']/div") #list of web elements
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()

cart = driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']")
cart.click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

price1 = int(driver.find_element(By.CSS_SELECTOR,"p[css='2']").text)
price2 = int(driver.find_element(By.CSS_SELECTOR,"p[css='4']").text)
price3 = int(driver.find_element(By.CSS_SELECTOR,"p[css='6']").text)
prices = price1+price2+price3
print(prices)
totalamount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert prices == totalamount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
#here instead of having sleep we can use implicit wait and explicit wait,
# bcoz it is not good to have sleep in selenium code
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()