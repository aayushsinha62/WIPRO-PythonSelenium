#grouping - set of testcases run together - issues fixed in that particular module

import pytest


# testcase1
@pytest.mark.sanity  #sanity - narrow testing done in build to proceed for further testing
def testcase1():
    print("Testcase1 is executed")


# testcase2
@pytest.mark.regression  #regression broad testing to check if anything previously built broke
def testcase2():
    print("Testcase2 is executed")


# testcase3
def test_case3():
    print("Testcase3 is executed")