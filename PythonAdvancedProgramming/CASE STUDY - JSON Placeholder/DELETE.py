import requests

def test_delete_post(base_url):
    response = requests.delete(f"{base_url}/posts/1")

    assert response.status_code == 200
