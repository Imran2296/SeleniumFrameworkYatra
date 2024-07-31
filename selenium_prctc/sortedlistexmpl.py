import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#empty list created
newsortedlist = []
service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#Click on column header
driver.find_element(By.CSS_SELECTOR,"th:nth-child(1)").click()
#collect all veggie names ->newsortedlist(A,B,C)
browsersortlist = driver.find_elements(By.XPATH,"//tr/td[1]")
for elements in browsersortlist:
    newsortedlist.append(elements.text)

originalbrowserlist = newsortedlist.copy()
#sort this newsortedlist -> updated list -> (A,B,C)
newsortedlist.sort()

time.sleep(4)