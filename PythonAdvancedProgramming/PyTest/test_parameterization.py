#parameterization : testing multiple set of test data with the same function

#@pytest.mark.parameterize()

#no parameters used

def test_Add1():
    assert 2+3==5

def test_Add2():
    assert 4+5==9

import pytest

    #multiple parameters
@pytest.mark.parametrize("a,b,result",[(2,3,5),(4,5,9),(10,1,19)])

def test_add(a,b,result):
    assert a+b==result

#single parameter
@pytest.mark.parametrize("number",[1,2,3,4,5])
def test_even(number):
    assert number%2==0


# dictionary items
@pytest.mark.parametrize("payload", [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 17}
])
def test_create_user(payload):
    assert payload["age"] > 18