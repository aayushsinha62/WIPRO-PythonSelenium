#skip - if defects are there
#skip - if the testcases are absolute //feature is removed
#windows, mobile OS dependency
#browsers -

import pytest


# testcase1
def testcase1():
    print("Testcase1 is executed")


# testcase2
@pytest.mark.skip   #skips test case
def testcase2():
    print("Testcase2 is executed")


# testcase3

def test_case3():
    print("Testcase3 is executed")