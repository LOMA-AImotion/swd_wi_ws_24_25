import pytest
from num_zeros import num_zeros

def test_num_zeros_empty_list():
    assert num_zeros([]) == 0

def test_num_zeros_no_zeros():
    assert num_zeros([1, 2, 3, 4, 5]) == 0

def test_num_zeros_all_zeros():
    assert num_zeros([0, 0, 0, 0, 0]) == 5

def test_num_zeros_some_zeros():
    assert num_zeros([1, 0, 2, 0, 3, 0, 4]) == 3

def test_num_zeros_single_zero():
    assert num_zeros([0]) == 1

def test_num_zeros_zero_at_start():
    assert num_zeros([0, 1, 2, 3, 4]) == 1

def test_num_zeros_zero_at_end():
    assert num_zeros([1, 2, 3, 4, 0]) == 1

if __name__ == "__main__":
    pytest.main()