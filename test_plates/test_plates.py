from plates import is_valid
import pytest

def test_start():
    assert is_valid("ds") == True
    assert is_valid("A4") == False

def test_max():
    assert is_valid("CS5025") == True
    assert is_valid("CS502550") == False

def test_min():
    assert is_valid("CS") == True
    assert is_valid("C") == False

def test_numberlast():
    assert is_valid("CS50A") == False

def test_firstzero():
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("CS50!") == False
