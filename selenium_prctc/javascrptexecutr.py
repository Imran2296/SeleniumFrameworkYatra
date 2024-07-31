import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#if we want execution in headless mode where we can't see invokation of url
#since it is headless mode we cannot see any chrome opening for execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
#if we want selenium to handle the ssl certificates which we get before opening url...
# like advanced and back to safty options
chrome_options.add_argument("--ignore-cerificate-errors--")

service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#driver.execute_script is javascript code that helps to execute javascript
#window.scrollBy(0,500) this is used yto scroll the page from range 0 to 500
#if we want to scroll page to the end, we can use "window.scrollBy(0,document.body.scrollHeight)"
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#with help of "driver.get_screenshot_as_file("screen.png)" we can take screenshot in
# whatever step the browser is
driver.get_screenshot_as_file("screen.png")

time.sleep(2)
