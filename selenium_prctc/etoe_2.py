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
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# other way to write CSS -> a[href*='shop'] and XPATH -> //a[contains(@href,'shop')]
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
Results = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for result in Results:
    productname = result.find_element(By.XPATH,"div/h4/a").text
    if productname == "Blackberry":
        result.find_element(By.XPATH,"//app-card[4]//div[1]//div[2]//button[1]").click()

driver.find_element(By.CSS_SELECTOR,".nav-link.btn.btn-primary").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Ind")
countries = driver.find_elements(By.CSS_SELECTOR,".suggestions")

for country in countries:
    if country.text == "India":
        country.click()

#driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"label[for='checkbox2'] a").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-info").click()
driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click()
successmsg = driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text
print(successmsg)
assert "Success! Thank you!" in successmsg