import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()

cart = driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']")
cart.click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
time.sleep(7) #here instead of having sleep we can use implicit wait and explicit wait,
# bcoz it is not good to have sleep in selenium code
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()

#instead of putting multiple sleeps we can use implicit and explicit mechanism in selenuim
#implicit wait is like global timeout,
# if any element is not shown on the page,it will wait for max of given (5) seconds for that to show up.
#it does not blindly wait for 5 secs, if the element shows up in 2 secs, it will immediately execute
#saving u 3secs.
#in case of sleep, if give 5 secs it will wait for 5 secs even if codes executes in 2 secs,
#wasting your 3 secs.