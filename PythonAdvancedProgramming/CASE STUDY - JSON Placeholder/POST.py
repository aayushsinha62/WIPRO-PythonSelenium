import requests

def test_create_post(base_url):
    payload = {
        "title": "API Testing",
        "body": "Testing POST request",
        "userId": 1
    }

    response = requests.post(f"{base_url}/posts", json=payload)

    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]
