from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CountryPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.XPATH, "(//select)[1]")
    #dropdown = Select(self.driver.find_element(By.XPATH, "(//select)[1]"))
    #dropdown.select_by_value("India")
    checkbox = (By.CSS_SELECTOR, ".chkAgree")
    submit = (By.XPATH, "//button[text()='Proceed']")

    #self.driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
    #self.driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

    def getCountry(self):
        return Select(self.driver.find_element(*CountryPage.country))

    def getCheckbox(self):
        return self.driver.find_element(*CountryPage.checkbox)

    def getSubmit(self):
        return self.driver.find_element(*CountryPage.submit)

