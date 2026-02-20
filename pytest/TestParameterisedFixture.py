import pytest

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    print("Current Browser:", request.param)
    return request.param

def testbrowser(browser):
    assert browser in ["chrome", "firefox"]
