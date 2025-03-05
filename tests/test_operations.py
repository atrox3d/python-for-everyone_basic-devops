from calculator.operations import add, subtract


def test_add():
    assert add(4, 5) == 9


def test_subtract():
    assert subtract(10, 5) == 5
