# 1.Write a test that is skipped because a feature is not implemented yet.
#
# 2.write a test that runs only on Linux and skips on Windows.
#
# 3.Write a test that checks an API health endpoint.
# If status code is not 200 → skip the test dynamically.
#
# 4.Mark a failing test as xfail with reason: "Bug #123".
#
# 5.You have 5 parameterized cases.
# 2 are known bugs.
# Mark only those 2 cases as xfail without marking entire test.


import sys
import pytest
import requests


# --------------------------------------------------
# 1. Skip test because feature is not implemented yet
# --------------------------------------------------

@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    assert True


# --------------------------------------------------
# 2. Run only on Linux, skip on Windows
# --------------------------------------------------

@pytest.mark.skipif(sys.platform == "win32",
                    reason="Test not supported on Windows")
def test_linux_only():
    assert True


# --------------------------------------------------
# 3. API health check
# Skip dynamically if status code is not 200
# --------------------------------------------------

def test_api_health_check():
    response = requests.get("https://httpbin.org/status/503")

    if response.status_code != 200:
        pytest.skip(f"Health check failed with status {response.status_code}")

    assert response.status_code == 200


# --------------------------------------------------
# 4. Mark a failing test as xfail with reason "Bug #123"
# --------------------------------------------------

@pytest.mark.xfail(reason="Bug #123")
def test_known_bug():
    assert 1 == 2


# --------------------------------------------------
# 5. Parameterized test
# 5 cases, 2 known bugs marked as xfail
# --------------------------------------------------

@pytest.mark.parametrize(
    "input_value,expected",
    [
        (1, 1),
        (2, 2),
        pytest.param(3, 99, marks=pytest.mark.xfail(reason="Bug #201")),
        pytest.param(4, 100, marks=pytest.mark.xfail(reason="Bug #202")),
        (5, 5),
    ]
)
def test_param_cases(input_value, expected):
    assert input_value == expected
