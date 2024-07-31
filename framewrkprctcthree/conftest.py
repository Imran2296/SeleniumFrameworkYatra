import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("C:\\Webdrivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(4)
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    request.cls.driver = driver # if we write this statement, then we need not return anything
    #there need to be connection between driver of conftest and test_greenKart.
    yield
    driver.close()