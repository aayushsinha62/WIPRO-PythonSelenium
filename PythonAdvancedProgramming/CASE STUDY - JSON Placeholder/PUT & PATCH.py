import requests

def test_put_update_post(base_url):
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }

    response = requests.put(f"{base_url}/posts/1", json=payload)

    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


def test_patch_update_post(base_url):
    payload = {
        "title": "Patched Title"
    }

    response = requests.patch(f"{base_url}/posts/1", json=payload)

    assert response.status_code == 200
    assert response.json()["title"] == "Patched Title"
