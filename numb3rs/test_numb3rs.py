from numb3rs import validate

def test_simple():
    assert validate("127.0.0.1") == True

def test_short():
    assert validate("1.1.1") == False

def test_long():
    assert validate("1.1.1.1.1") == False

def test_nonip():
    assert validate("cats") == False

def test_big():
    assert validate("300.300.300.300") == False

def test_first():
    assert validate("127.300.300.300") == False
