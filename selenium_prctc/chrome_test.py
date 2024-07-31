import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F")

#ID, XPATH, CSSSELECTOR, classname,name, linktext etc

driver.find_element(By.NAME,'email').send_keys("immu@gmail.com")
#driver.find_element(By.ID,'pass').send_keys("imran1234")

# (xpath syntax) //tagname[@attribute='value'] -> //input[@type='submit']
# (CSSSELECTOR syntax)  tagname[attribute='value'] -> input[type='submit']
driver.find_element(By.CSS_SELECTOR,"INPUT[ID='pass']").send_keys("imran1234")
#driver.find_element(By.XPATH,"//input[@type='submit']").click()










time.sleep(6)
