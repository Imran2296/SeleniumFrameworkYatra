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
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
windowopend = driver.window_handles
driver.switch_to.window(windowopend[1])
print(driver.find_element(By.XPATH,"//a[text()='mentor@rahulshettyacademy.com']").text)
driver.switch_to.window(windowopend[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("mentor@rahulshettyacademy.com")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("1234imran")
driver.find_element(By.XPATH,"(//span)[3]").click()
dropdown = Select(driver.find_element(By.CSS_SELECTOR,"select[class='form-control']"))
dropdown.select_by_visible_text("Student")
driver.find_element(By.CSS_SELECTOR,"#terms").click()
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert.alert-danger.col-md-12")))
print(driver.find_element(By.CSS_SELECTOR,".alert.alert-danger.col-md-12").text)

time.sleep(5)



