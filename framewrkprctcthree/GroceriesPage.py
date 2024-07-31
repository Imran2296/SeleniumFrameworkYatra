from selenium.webdriver.common.by import By


class groceriesPage:

    def __init__(self, driver):
        self.driver = driver

    page = (By.CSS_SELECTOR, "div[class='IFZV3u']")
    search = (By.XPATH, "//span[text()='Shop now']")
    ghee = (By.CSS_SELECTOR, "input[placeholder='Search grocery products']")
    searchsubmit = (By.CSS_SELECTOR, "button[type='submit']")
    gheepage = (By.XPATH, "//img[@alt='Godrej Jersey Pure Cow Ghee 1 L Pouch (Neyyi)']")
    submitghee = (By.CSS_SELECTOR, "button[class='QqFHMw vslbG+ In9uk2 pKi72Z']")
    finalcart = (By.CSS_SELECTOR, "._9Wy27C")
    def getPage(self):
        return self.driver.find_element(*groceriesPage. page)

    def getSearch(self):
        return self.driver.find_element(*groceriesPage. search)

    def getGhee(self):
        return self.driver.find_element(*groceriesPage. ghee)

    def getSearchsubmit(self):
        return self.driver.find_element(*groceriesPage. searchsubmit)

    def getGheepage(self):
        return self.driver.find_element(*groceriesPage. gheepage)

    def getSubmitghee(self):
        return self.driver.find_element(*groceriesPage. submitghee)

    def getFinalcart(self):
        return self.driver.find_element(*groceriesPage. finalcart)

