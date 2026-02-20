import pytest

def div(a, b):
    if b == 0:
        raise ValueError("Divide by zero failed.")
    return a / b

def test_div_zero():
    with pytest.raises(ValueError) as exc_info:
        div(5, 0)
    assert str(exc_info.value) == "Divide by zero failed."
