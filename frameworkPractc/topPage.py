from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class topPages:

    def __init__(self, driver):
        self.driver = driver

    radiobtns = (By.CSS_SELECTOR, "input[value='radio2']")
    suggestions = (By.XPATH,"//input[@id='autocomplete']")
    dropdown = (By.CSS_SELECTOR,"#dropdown-class-example")
    checkbox = (By.CSS_SELECTOR,"#checkBoxOption2")
    #radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
    #radiobtns[1].click()


    def getRadiobtn(self):
        return self.driver.find_element(*topPages. radiobtns)

    def getSuggestions(self):
        return self.driver.find_element(*topPages. suggestions)

    def getDropdown(self):
        return Select(self.driver.find_element(*topPages. dropdown))

    def getCheckbox(self):
        return self.driver.find_element(*topPages. checkbox)
