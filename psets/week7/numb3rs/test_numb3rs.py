from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1000.3.2.1") == False
    assert validate("1000.1000.1000.1000") == False
    assert validate("1000") == False
    assert validate("275.3.6.28") == False
    assert validate("10.10.10.10") == True
    assert validate("1.1000.1000.1000") == False
    assert validate("1000.1000.1000.1") == False
    assert validate("10.10000.10000.10000") == False
    assert validate("10.1000.1000.1000") == False
    assert validate("255.256.256.256") == False