import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")
    # yield keyword help executing afterfixture tests
    yield
    print("I will be executed at last")

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)

