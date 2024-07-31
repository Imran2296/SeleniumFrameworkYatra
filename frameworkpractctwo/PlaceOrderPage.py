from selenium.webdriver.common.by import By


class PlaceOrder:

    def __init__(self, driver):
        self.driver = driver

    promoCode = (By.CSS_SELECTOR, ".promoCode")
    apply = (By.CSS_SELECTOR, ".promoBtn")
    orderPlace = (By.XPATH, "//button[text()='Place Order']")

    def getPromocode(self):
        return self.driver.find_element(*PlaceOrder. promoCode)

    def getApplycode(self):
        return self.driver.find_element(*PlaceOrder. apply)

    def getOrderplace(self):
        return self.driver.find_element(*PlaceOrder. orderPlace)