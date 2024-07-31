from selenium.webdriver.common.by import By


class MobilePage:

    def __init__(self, driver):
        self.driver = driver

    mobiles = (By.CSS_SELECTOR,"img[alt='Mobiles']")
    alliphones = (By.XPATH, "//div[@class='X8l5DD']//div[1]//a[1]//div[1]//img[2]")
    iphone = (By.XPATH, "//div[normalize-space()='Apple iPhone 14 Plus (Blue, 128 GB)']")

    def getMobilePage(self):
        return self.driver.find_element(*MobilePage. mobiles)

    def getAlliphones(self):
        return self.driver.find_element(*MobilePage. alliphones)

    def getIphone(self):
        return self.driver.find_element(*MobilePage. iphone)

