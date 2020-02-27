def add(a, b):
    return a + b
#comment


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
