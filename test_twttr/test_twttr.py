from twttr import shorten
import pytest

def test_word():
    assert shorten("This is twitter") == "Ths s twttr"

def test_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_numbers():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("./!?-") == "./!?-"

def test_intfloat():
    with pytest.raises(TypeError):
        shorten(123)
    with pytest.raises(TypeError):
        shorten(1.2)
