from main import add


def test_add():
    assert add(1, 2) == 3
    assert add(1.0, 2.0) == 3.0
    assert add(1, 2.0) == 3.0
    assert add(1.0, 2) == 3.0

