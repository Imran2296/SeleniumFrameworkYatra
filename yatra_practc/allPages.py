from selenium.webdriver.common.by import By


class AllPages:

    def __init__(self, driver):
        self.driver = driver

    fromPlace = (By.XPATH, "//input[@name='flight_origin' and @id='BE_flight_origin_city']")
    toPlace = (By.XPATH, "//input[@name='flight_destination' and @id='BE_flight_arrival_city']")
    originDate = (By.XPATH, "//input[@id='BE_flight_origin_date']")
    selectOriginDate = (By.XPATH, "//td[@data-date='06/08/2024']")
    studentFare = (By.XPATH, "//a[normalize-space()='Student Fare']")
    nonStopFlight = (By.XPATH, "//a[normalize-space()='Non Stop Flights']")
    searchFlight = (By.XPATH, "//input[@type='submit' and @value='Search Flights']")
    bookFlight = (By.XPATH, "(//button[@class='fs-14 secondary-button select-button button border-thin cursor-pointer bold'][normalize-space()='Book Now'])[1]")

    def getFromPlace(self):
        return self.driver.find_element(*AllPages. fromPlace)

    def getToPlace(self):
        return self.driver.find_element(*AllPages. toPlace)

    def getOriginiDate(self):
        return self.driver.find_element(*AllPages. originDate)

    def getSelectOriginDate(self):
        return self.driver.find_element(*AllPages. selectOriginDate)

    def getStudentFare(self):
        return self.driver.find_element(*AllPages. studentFare)

    def getNonStopFlight(self):
        return self.driver.find_element(*AllPages. nonStopFlight)

    def getSearchFlight(self):
        return self.driver.find_element(*AllPages. searchFlight)

    def getBookFlight(self):
        return self.driver.find_element(*AllPages. bookFlight)

