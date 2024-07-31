import time
import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/?ref_=nav_custrec_signin&")
driver.maximize_window()
#action = ActionChains(driver)
#action.move_to_element(driver.find_element(By.CSS_SELECTOR,"span[class='nav-line-2 ']")).perform()
#driver.find_element(By.CSS_SELECTOR,"div[id='nav-flyout-ya-signin'] span[class='nav-action-inner']").click()

#email login
#driver.find_element(By.ID,"ap_email_login").send_keys("imransk.edu@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"#continue").click()
#password
#driver.find_element(By.CSS_SELECTOR,"#ap_password").send_keys("Immu199608")
#driver.find_element(By.XPATH,"//input[@id='signInSubmit']").click()
#search page
driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox").send_keys("shirts for men")
driver.find_element(By.CSS_SELECTOR,"#nav-search-submit-button").click()

#driver.execute_script("window.scrollBy(0,500);")

#driver.find_element(By.XPATH,"(//i[@class='a-icon a-icon-checkbox'])[3]").click()
driver.find_element(By.XPATH,"(//i[@class='a-icon a-icon-checkbox'])[4]").click()
driver.find_element(By.XPATH,"(//i[@class='a-icon a-icon-checkbox'])[5]").click()

driver.find_element(By.XPATH,"(//a[@class='a-link-normal s-no-outline'])[1]").click()

windowopened = driver.window_handles
driver.switch_to.window(windowopened[0])

driver.find_element(By.LINK_TEXT,"Today's Deals").click()

#driver.execute_script("window.scrollBy(0,2000);")

driver.find_element(By.CSS_SELECTOR,"div[aria-label='Apple iPhone 13 (128GB) - Midnight'] div[class='a-section ProductCardImage-module__wrapper_YgLz4kq6ekChj01qeqOf']").click()

driver.execute_script("window.scrollBy(0,400);")
driver.find_element(By.CSS_SELECTOR,"img[alt='Green']").click()
driver.find_element(By.CSS_SELECTOR,"#a-autoid-21").click()
#driver.find_element(By.CSS_SELECTOR,"#mbb-offeringID-1").click()
driver.implicitly_wait(5)
#driver.find_element(By.XPATH,"(//input[@id='add-to-cart-button'])[2]").click()

#driver.find_element(By.CSS_SELECTOR,"//input[@aria-labelledby='attach-sidesheet-checkout-button-announce']").click()
#driver.execute_script("arguments[0].scrollIntoView(true)", scrollto)
driver.execute_script("window.scrollBy(0,100);")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@id='add-to-cart-button'])[2]").click()



time.sleep(4)
