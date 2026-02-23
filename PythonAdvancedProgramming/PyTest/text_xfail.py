#xfail is a marker used to indicate that a test is expected to fail due to a known issue (e.g., a bug or an unimplemented feature)
import sys
import pytest

@pytest.mark.xfail(reason="Known bug in the third-party library")
def test_function_with_bug():
    assert (1 + 1) == 3 # This assertion will fail as expected

# testcase1
@pytest.mark.sanity
def testcase1():
    print("Testcase1 is executed")

# testcase2
@pytest.mark.regression
def testcase2():
    print("Testcase2 is executed")

# testcase3
@pytest.mark.db
def testcase3():
    print("Testcase3 is executed")


# xfail with a condition

#strict false, even though testcase condition fails but the testcase is passed
#but the condition inside xfail should pass else xfail won't apply and it will act as a normal testcase

@pytest.mark.xfail(sys.platform == "win32",
                   reason="Known bug on Windows")
def test_login_feature():
    assert False


#strict true, even though testcase condition passes but the testcase is failed
@pytest.mark.xfail(sys.platform == "win32",
                   strict=True,
                   reason="Bug #101 not fixed yet on Windows")
def test_login_feature_strict():
    assert True

