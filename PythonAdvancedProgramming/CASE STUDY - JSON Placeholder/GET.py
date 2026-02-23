import requests

def test_get_all_posts(base_url):
    response = requests.get(f"{base_url}/posts")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_get_single_post(base_url):
    response = requests.get(f"{base_url}/posts/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_invalid_post(base_url):
    response = requests.get(f"{base_url}/posts/9999")

    assert response.status_code == 404

