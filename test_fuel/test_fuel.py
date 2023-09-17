from fuel import convert, gauge
import pytest

def test_convert_simple():
    assert convert("1/2") == 50

def test_convert_type():
    assert type(convert("1/2")) == int

def test_gauge_percentage():
    assert "%" in gauge(50)

def test_gauge_F():
     assert gauge(99) == "F"
     assert gauge(100) == "F"

def test_gauge_E():
     assert gauge(1) == "E"
     assert gauge(0) == "E"

def test_errors():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
