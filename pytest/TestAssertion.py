import pytest_check as check

def test_add():

def test_equal():
    assert 1 == 1

def test():
    assert 1 == 2
    print("Hello")


def test_list():
    fruits = ["apple", "banana", "cherry"]
    assert "banana" in fruits

def test_dict():
    creds = {"username": "username", "password": "password"}
    assert creds["password"] == "admin123"

def test_compareList():
    assert [1,2,3] == [1,2,3]

def test_custommsg():
    result = 10
    assert result == 10 , "Result should be 5"


def test_multiple():
    check.equal(1,2)
    check.equal(3,4)