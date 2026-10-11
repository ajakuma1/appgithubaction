def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(4, 3) == 1
    assert subtract(3, 3) == 0
    