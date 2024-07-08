"""Module for linear search"""


def linear_search(arr: list[int], target: int) -> bool:
    """Linear seach algorithm"""
    for i in arr:
        if i == target:
            return True
    return False


def linear_search_return_index(arr: list[int], target: int) -> int:
    """
    - Linear search algorithm returns index if element is found
    - Returns -1 if not found
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
