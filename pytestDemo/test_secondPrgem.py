#you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip test case with @pytest.mark.skip
import pytest

#@pytest.mark.smoke
# @pytest.mark.skip
#@pytest.mark.xfail ->you want this test case to fail but don;t want it in reports
def test_immuone():
    msg = "hello"
    assert msg == "Hi","Test failed bcoz string do not match"


def test_immutwo():
    a=4
    b=6
    assert a+2 == 6, "Addition do not match"






