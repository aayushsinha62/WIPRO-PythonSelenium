#fixture dependency - second fixture will work only when the first fixture runs

import pytest

#fixtures can be put on in conftest file
@pytest.fixture()
def fixture_a():
    return "Data from A"

@pytest.fixture()
def fixture_b(fixture_a): #calling fixture a
    return f"{fixture_a}+Data from B"


def test(fixture_b):
    assert fixture_b=="Data from A+Data from B"

    #hierarchy - fixture a then b then test