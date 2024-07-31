import pytest
import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class") #scope to the class level
def setup(): #when u declare one fixture, we will have request as an instance
        service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(4)
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()