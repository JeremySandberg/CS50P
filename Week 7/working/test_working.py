import pytest
from working import convert

def test_default():
    assert convert("8 AM to 7 PM") == "08:00 to 19:00"
    assert convert("8 AM to 7:30 PM") == "08:00 to 19:30"
    assert convert("8:20 AM to 7 PM") == "08:20 to 19:00"
    assert convert("8:20 AM to 7:30 PM") == "08:20 to 19:30"

def test_edgecases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:12 AM to 12:12 PM") == "00:12 to 12:12"

def test_errors_format():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("12 AM - 12 PM")
    with pytest.raises(ValueError):
        convert("12 AM to 6 PM to 12 PM")

def test_errors_edgecases():
    with pytest.raises(ValueError):
        convert("13 AM to 13:33 AM")
    with pytest.raises(ValueError):
        convert("13 PM to 13:33 PM")
