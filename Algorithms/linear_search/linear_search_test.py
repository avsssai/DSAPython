"""Module for testing linear search"""

from linear_search import linear_search, linear_search_return_index
import pytest


def test_linear_search():
    """Testing linear search"""
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 1) is True
    assert linear_search(arr, 2) is True
    assert linear_search(arr, 3) is True
    assert linear_search(arr, 4) is True
    assert linear_search(arr, 5) is True
    assert linear_search(arr, 53) is False


def test_linear_search_index():
    """Testing linear search - returns index"""
    arr = [1, 2, 3, 4, 5]
    assert linear_search_return_index(arr, 1) == 0
    assert linear_search_return_index(arr, 2) == 1
    assert linear_search_return_index(arr, 5) == 4
    assert linear_search_return_index(arr, 53) == -1


if __name__ == "__main__":
    pytest.main()
