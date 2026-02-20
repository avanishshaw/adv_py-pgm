# Fixture are the pieces of code which are run before the test case or after the test case
import pytest

@pytest.fixture
def simple_data():
    return 45

# testcase using the simple fixture
def testcase1(simple_data):
    assert simple_data == 45

@pytest.fixture()
def api_url():
    return "http://api.example.com"

def test_api(api_url):
    assert "https" in api_url

