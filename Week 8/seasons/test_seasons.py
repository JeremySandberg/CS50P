from seasons import date_to_minutes
import pytest

def test_default():
    pass

def test_errors():
    with pytest.raises(SystemExit):
        date_to_minutes("February 3rd 1999")