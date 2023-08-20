from bank import value

def test_0():
    assert value("hello") == 0


def test_20():
    assert value("howdy") == 20

def test_100():
    assert value("what is up") == 100
    assert value("What's up!") == 100

def test_upper():
    assert value("HELLO") == 0
    