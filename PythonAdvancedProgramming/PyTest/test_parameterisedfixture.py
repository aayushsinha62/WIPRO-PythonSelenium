import pytest

#request - pytest object that contains information about
#       who is calling the fixture and with what data

@pytest.fixture(params=["Chrome","Firefox"])
def browser(request):
    print("Current browser:",request.param)
    return request.param

def testbrowser(browser):
    assert browser in ["Chrome","Firefox"]


#Selecting even or odd number


@pytest.fixture(params=[1,2,3,34,5,6,7,8])
def number(request):
    return request.param

def test_evenodd(number):
    assert number%2==0
