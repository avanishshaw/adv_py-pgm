import requests


def test_get_profile(base_url, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(base_url, headers=headers)
    assert response.status_code == 200

def test_get_orders(base_url, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{base_url}/orders", headers=headers)
    assert response.status_code == 200

