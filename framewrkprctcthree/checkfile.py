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
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(4)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"div[aria-label='Fashion']")).perform()
time.sleep(6)
