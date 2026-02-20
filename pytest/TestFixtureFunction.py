import pytest

@pytest.fixture()
def openbrowser():
    print("\nOpen Browser")
    yield
    print("Close Browser After Test")


@pytest.fixture()
def closebrowser():
    print("\nPreparing to Logout")
    yield
    print("Cleanup After Logout")


@pytest.mark.usefixtures("openbrowser")
def test_login():
    print("Enter the username")
    print("Enter the password")
    print("Click on the login button")


@pytest.mark.usefixtures("closebrowser")
def test_logout():
    print("User is logged out")
#fixture at class level
#fixture at module level
#fixture at session level