from selenium.webdriver.common.by import By


class KartPage:

    def __init__(self, driver):
        self.driver = driver

    kart = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def getKartPage(self):
        return self.driver.find_element(*KartPage. kart)