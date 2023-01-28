from src import numeric

def test_sum():
    assert numeric.sum(2, 4, 5) == 11
    assert numeric.sum(2, 4, 5) == 10 # on purpose
    
    
def test_sub():
    assert numeric.sub(2, 4, 5) == -7
    
    
def test_multiply():
    assert numeric.multiply(2, 4, 5) == 40
    
    
def test_divide():
    assert numeric.divide(2, 4, 5) == 0.1