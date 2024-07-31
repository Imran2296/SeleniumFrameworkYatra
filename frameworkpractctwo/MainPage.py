from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    search = (By.CSS_SELECTOR, ".search-keyword")

    def getSearch(self):
        return self.driver.find_element(*MainPage. search)