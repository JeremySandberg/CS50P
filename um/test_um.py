import pytest
from um import count

def test_default():
    assert count("Yummy") == 0
    assert count("um") == 1
    assert count("umum") == 0
    assert count("You are, um, not me, um.") == 2
    assert count("um!") == 1
    assert count(".um!") == 1
    assert count("UM") == 1
    assert count("uM") == 1
