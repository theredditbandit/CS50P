from jar import Jar
import pytest

def test_init():
    jar = Jar(12)
    assert jar.capacity == 12
    assert jar.cookie == "🍪"
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar2 = Jar(-14)


def test_str():
    jar = Jar(12)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar3 = Jar(11)
    jar3.deposit(1)
    assert jar3.size == 1
    jar3.deposit(1)
    assert jar3.size == 2

    with pytest.raises(ValueError):
        jar3.deposit(100)

    with pytest.raises(ValueError):
        jar3.deposit(-1)



def test_withdraw():
    jar4 = Jar(12)
    jar4.deposit(12)
    assert jar4.size == 12
    jar4.withdraw(2)
    assert jar4.size == 10

    with pytest.raises(ValueError):
        jar4.withdraw(11)

    with pytest.raises(ValueError):
        jar4.withdraw(-2)
