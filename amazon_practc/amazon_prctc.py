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

driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shirts")
driver.find_element(By.CSS_SELECTOR,"#nav-search-submit-button").click()
driver.execute_script("window.scrollBy(0,300)")
#driver.find_element(By.CSS_SELECTOR,"div[class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1'] span[class='a-size-medium a-color-base a-text-normal']").click()
driver.find_element(By.CSS_SELECTOR,"div[class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1'] a[class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']").click()
time.sleep(4)
windowopens = driver.window_handles
driver.switch_to.window(windowopens[1])
driver.execute_script("window.scrollBy(0,500)")
dropdown = Select(driver.find_element(By.NAME,"dropdown_selected_size_name"))
dropdown.select_by_visible_text("S")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#add-to-cart-button").click()
driver.find_element(By.XPATH,"//a[@href='/cart?ref_=sw_gtc']").click()
driver.find_element(By.XPATH,"(//span[@class='a-label a-checkbox-label'])[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[@class='a-dropdown-label']").click()
driver.find_element(By.CSS_SELECTOR,"#quantity_1").click()

time.sleep(5)