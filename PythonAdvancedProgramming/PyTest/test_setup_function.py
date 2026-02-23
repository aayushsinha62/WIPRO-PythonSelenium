#function level setup and tear down
#these run before and after each test function
import pytest
#setup at a function level
def setup_function(function):
    print("opening the browser")

#teardown up at a function level

def teardown_function(function):
    print("closing the browser")

#testcase1

def testcase1():
    print("Testcase1 is executed")

#testcase2
@pytest.mark.regression
def testcase2():
    print("Testcase2 is executed")

#testcase3
@pytest.mark.sanity
def test_case3():
    print("Testcase3 is executed")
