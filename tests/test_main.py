# Testing exceptions
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# Testing lists
def test_list_operations():
    my_list = [1, 2, 3]
    assert len(my_list) == 3
    assert 2 in my_list
    assert my_list[0] == 1

# Grouping related tests
class TestMathOperations:
    def test_addition(self):
        assert 1 + 1 == 2
    
    def test_subtraction(self):
        assert 3 - 1 == 2