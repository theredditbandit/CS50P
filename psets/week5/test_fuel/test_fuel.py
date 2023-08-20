import pytest
from fuel import convert , gauge

def test_convert_ZeroDivision():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_convert_ValueError():
    with pytest.raises(ValueError):
        convert("cat/dog")

# def test_gauge_ValueError():
#     with pytest.raises(ValueError):
#         gauge("cat")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"

def test_convert():
    assert convert("50/100") == 50
    assert convert("0/100") == 0
    assert convert("100/100") == 100
