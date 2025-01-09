import pytest
from subsample_to_half import subsample_to_half

def test_subsampling_empty_list():
    assert subsample_to_half([]) == []

def test_subsampling_even():
    assert subsample_to_half([1,2,3,4,5,6,7,8]) == [1, 3]

def test_subsampling_odd():
    assert subsample_to_half([1,2,3,4,5,6,7,8,9]) == [1,3]

def test_subsampling_lecture():
    assert subsample_to_half([3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]) == [3.2, 2.8, 6.4]

if __name__ == "__main__":
    pytest.main()