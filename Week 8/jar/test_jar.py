from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar2 = Jar(5)
    assert jar2.capacity == 5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(11)
    assert jar.size == 11
    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)
