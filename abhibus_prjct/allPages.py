from selenium.webdriver.common.by import By


class allabhibus:

    def __init__(self, driver):
        self.driver = driver

    fromLocation = (By.XPATH,"//input[@placeholder='From Station']")
    toLocation = (By.XPATH, "//input[@placeholder='To Station']")
    date = (By.XPATH, "//div/button[text()='Tomorrow']")
    filterOne = (By.XPATH, "//div[contains(@class,'row filter-wrapper')]//a[1]")
    filterTwo = (By.CSS_SELECTOR, "#price-drop")
    busBrand = (By.XPATH,"//div/img[@src='https://static.abhibus.com/offerbanners/Jun2024/26/1719399172/streamlinebus.webp']")
    seat = (By.XPATH, "//button[text()='Show Seats']")
    seatSelection = (By.XPATH,"//table[@id='seat-layout-details'][1]/tbody/tr[2]/td[3]/div/button/span[text()='C1']")
    boadringPoint = (By.CSS_SELECTOR, "input[placeholder='Search Boarding Point']")
    boardingpointOne = (By.XPATH, "//div/p[text()='Kondapur (Pickup Van/Bus)']")
    droppingPoint = (By.CSS_SELECTOR, "input[placeholder='Search Dropping Point']")
    droppingPointOne = (By.XPATH, "//div/p[text()='Silk Board']")
    selectSeat = (By.XPATH, "//div[text()='Selected Seat']")
    def getFromLoc(self):
        return self.driver.find_element(*allabhibus. fromLocation)

    def getToLoc(self):
        return self.driver.find_element(*allabhibus. toLocation)

    def getDate(self):
        return self.driver.find_element(*allabhibus. date)

    def getFilterOne(self):
        return self.driver.find_element(*allabhibus. filterOne)

    def getFilterTwo(self):
        return self.driver.find_element(*allabhibus. filterTwo)

    def getBusType(self):
        return self.driver.find_element(*allabhibus. busBrand)

    def getSeat(self):
        return self.driver.find_element(*allabhibus. seat)

    def getSeatSelect(self):
        return self.driver.find_element(*allabhibus. seatSelection)

    def getBoardingPoint(self):
        return self.driver.find_element(*allabhibus. boadringPoint)

    def getBoardingPointOne(self):
        return self.driver.find_element(*allabhibus. boardingpointOne)

    def getDroppingPoint(self):
        return self.driver.find_element(*allabhibus. droppingPoint)

    def getDroppingPointOne(self):
        return self.driver.find_element(*allabhibus. droppingPointOne)

    def getSelectSeat(self):
        return self.driver.find_element(*allabhibus. selectSeat)