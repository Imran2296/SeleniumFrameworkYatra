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
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH,"//a[text()='Click Here']").click()

#here we need to clearly tell selenium that we have to print text from child window but not parent window
#with the help of window handles we can do it,it creates a list of windows opened like [0]- parent window
# [1]- child window and so on.
windowopened = driver.window_handles
#switch_to foucuses on the specified window
driver.switch_to.window(windowopened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
#with driver.close() we can close child window and work on parent window
driver.close()
#if we want to print output from parent window, we can give same method with valid list which is windowopened[0]
driver.switch_to.window(windowopened[0])
print(driver.find_element(By.XPATH,"//h3[text()='Opening a new window']").text)

