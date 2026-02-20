import pytest
import requests

from LabSessions.API_Automation.HTML_Parsing.Q2 import response


@pytest.fixture(scope='session')
def base_url():
    return 'http://127.0.0.1:5000'

@pytest.fixture(scope='session')
def auth_token(base_url):
    print("Getting auth token...")

    response = requests.post(
        f"{base_url}/login",
        json={"username": "admin", "password": "admin123"}
    )

    token = response.json()["token"]
    return token
