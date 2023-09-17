from bank import value
import pytest

def test_0():
    assert value("hello") == 0
    assert value("HeLLo") == 0
    assert value("hello there, you") == 0

def test_20():
    assert value("He") == 20
    assert value("Here is the money") == 20
    assert value("how are you?") == 20

def test_100():
    assert value("Something") == 100
    assert value("What is this") == 100
    assert value("Ohello") == 100
