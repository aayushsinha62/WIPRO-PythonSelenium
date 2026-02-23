# 1. Write a pytest fixture that generates an authentication token once per session and use it in multiple API test cases.
# 2. Create a fixture that creates a test user via API before a test and deletes the user after test execution using yield.
# 3. Write a test that validates JSON response schema from an API endpoint.
# 4. Implement a parametrized test that validates multiple HTTP status codes (200, 400, 401, 500).
# 5. Create a fixture chain: base_url -> auth_token -> user -> test case. Explain execution

import pytest
import requests
from jsonschema import validate

# -------------------------
# 1. Base URL fixture
# -------------------------
@pytest.fixture(scope="session")
def base_url():
    return "https://api.example.com"


# -------------------------
# 2. Session-scoped auth token fixture
# -------------------------
@pytest.fixture(scope="session")
def auth_token(base_url):
    response = requests.post(
        f"{base_url}/auth/login",
        json={"username": "test", "password": "secret"}
    )
    response.raise_for_status()
    return response.json()["access_token"]


# -------------------------
# 3. Create & delete user using yield
# -------------------------
@pytest.fixture
def user(base_url, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    # setup
    create_response = requests.post(
        f"{base_url}/users",
        json={"name": "pytest-user", "email": "pytest@test.com"},
        headers=headers
    )
    create_response.raise_for_status()
    user_data = create_response.json()

    yield user_data

    # teardown
    requests.delete(
        f"{base_url}/users/{user_data['id']}",
        headers=headers
    )


# -------------------------
# 4. Validate JSON response schema
# -------------------------
def test_user_schema(user):
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "email": {"type": "string"}
        },
        "required": ["id", "name", "email"]
    }

    validate(instance=user, schema=schema)


# -------------------------
# 5. Parametrized test for HTTP status codes
# -------------------------
@pytest.mark.parametrize("status_code", [200, 400, 401, 500])
def test_status_codes(base_url, status_code):
    response = requests.get(f"{base_url}/status/{status_code}")
    assert response.status_code == status_code


# -------------------------
# Fixture execution order explanation:
# base_url -> auth_token -> user -> test
#
# pytest resolves fixtures bottom-up:
# 1. base_url provides API root
# 2. auth_token uses base_url (session-scoped)
# 3. user uses base_url + auth_token (function-scoped)
# 4. test executes
# 5. user teardown runs after test
# -------------------------
