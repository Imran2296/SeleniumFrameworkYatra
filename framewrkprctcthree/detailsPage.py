from selenium.webdriver.common.by import By


class DetailsPage:

    def __init__(self, driver):
        self.driver = driver

    pincode = (By.CSS_SELECTOR, "#pincodeInputId")
    confrmpincode = (By.CSS_SELECTOR, ".i40dM4")
    memory = (By.XPATH, "//a[text()='512 GB']")
    cart = (By.XPATH, "//button[text()='Add to cart']")
    def getPincode(self):
        return self.driver.find_element(*DetailsPage. pincode)

    def getConfrmpincode(self):
        return self.driver.find_element(*DetailsPage. confrmpincode)

    def getMemory(self):
        return self.driver.find_element(*DetailsPage. memory)

    def getCart(self):
        return self.driver.find_element(*DetailsPage. cart)