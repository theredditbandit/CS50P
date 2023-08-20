import pytest
from working import convert

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_omit_to():
    with pytest.raises(ValueError):
        convert("9 AM - 10 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 10:00 PM")

def test_ampm():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")