import pytest
from seasons import get_date


def test_get_date():
    assert get_date("1999-01-01") == [1999,1,1]
    assert get_date("2003-03-23") == [2003,3,23]

    with pytest.raises(SystemExit):
        get_date("") # no input

    with pytest.raises(SystemExit): # invalid input format
        get_date("January 1, 1999")
        get_date("1999,01,01")
        get_date("2003,0323")

    with pytest.raises(SystemExit):
        get_date("0000-3-03") # invalid year
        get_date("2003-23-03") #invalid month
        get_date("2003-03-32") # invalid date