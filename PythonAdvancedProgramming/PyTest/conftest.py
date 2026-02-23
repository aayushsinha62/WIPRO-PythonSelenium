#conftest - a place to store all fixtures
#used by tests within its directory and subdirectories
import pytest

# -------------------------
# Function-level fixture
# -------------------------
@pytest.fixture(scope="function")
def function_setup():
    print("\n[FUNCTION] User logged in")
    yield
    print("[FUNCTION] User logged out")


# -------------------------
# Class-level fixture
# -------------------------
@pytest.fixture(scope="class")
def class_setup():
    print("\n[CLASS] Setup before class") # yield make it run before test
    yield
    print("\n[CLASS] Teardown after class") #yield make it run after test
            #without yield automatic teardown happens

# -------------------------
# Module-level fixture
# -------------------------
@pytest.fixture(scope="module")
def module_setup():
    print("\n[MODULE] Setup before module")
    yield
    print("\n[MODULE] Teardown after module")


# -------------------------
# Session-level fixture
# -------------------------
@pytest.fixture(scope="session")
def session_setup():
    print("\n[SESSION] Test session started")
    yield
    print("\n[SESSION] Test session finished")