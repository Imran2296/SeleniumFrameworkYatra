import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@id='checkBoxOption2']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        break

#radiobtns = driver.find_elements(By.XPATH,"//input[@value='radio3']")
#print(len(radiobtns))

radiobtns = driver.find_elements(By.CSS_SELECTOR,"input[name='radioButton']")
radiobtns[2].click() #when we know that positions of options do not change, no need to use for loop
assert radiobtns[2].is_selected() #is_selected will help you know if that radio button is selected or not

#is displayed
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
# is_displayed method will tell if that is displayed on screen or not,
# it will return true if displayed and false if not displayed.

#


# .classname will turnout to be cssselector

#for radio in radiobtns:
# if radio.get_attribute("value") == "radio3":
#     radio.click()
#    break


dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#dropdown-class-example"))
dropdown.select_by_index(2)


time.sleep(10)
