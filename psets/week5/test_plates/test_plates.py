from plates import is_valid

def test_valid():
    valid = ["CS50","cs50","CS3456"]
    for i in valid:
        assert is_valid(i) == True

def test_invalid():
    invalid = ["CS05","P13.14","H","OUTATIME","1234567","CS05p"]
    for i in invalid:
        assert is_valid(i) == False

def test_numplacement():
    assert is_valid("CS05P") == False
    assert is_valid("AAA222AA") ==  False
    assert is_valid("AA02") == False
    assert is_valid("AA22A") == False
    assert is_valid("50") ==  False

def test_alphabet():
    assert is_valid("12345") == False

def test_alnum():
    assert is_valid("12CS") == False
    assert is_valid("CSSS") == True
    assert is_valid("CS00") == False
    assert is_valid("CSAA22") == True
    assert is_valid("A-113") == False
    assert is_valid("SPEED") == True
    assert is_valid("5P33D") == False

def test_alnum_2():
    assert is_valid("53ed") ==  False
    assert is_valid("H") == False
    assert is_valid("HH33") == True
    assert is_valid("ECTO99") == True
    assert is_valid("ECT099") == False
    assert is_valid("NRVOUS") == True
    assert is_valid("1234") == False
    assert is_valid("NRV.OS") == False
    assert is_valid("NR505") == True
