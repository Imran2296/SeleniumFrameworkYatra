import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will execute at last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Imran","Shaik","rahulshettyacademy.com"]

@pytest.fixture(params=["chrome","Firefox","IE"])
def crossBrowser(request):
    return request.param
