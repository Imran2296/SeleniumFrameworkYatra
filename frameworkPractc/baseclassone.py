import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


class BaseClassOne:
    @pytest.fixture()
    def setup(self):
        service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_obj)
        self.driver.implicitly_wait(4)
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        self.driver.maximize_window()
