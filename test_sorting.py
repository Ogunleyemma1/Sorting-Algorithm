import pytest
from sorting import quick_sort, counting_sort

def test_quick_sort_empty():
    # Test empty list
    arr = []
    expected = []
    sorted_arr = quick_sort(arr)
    assert sorted_arr == expected

def test_quick_sort_single():
    # Test single element list
    arr = [1]
    expected = [1]
    sorted_arr = quick_sort(arr)
    assert sorted_arr == expected

def test_quick_sort_sorted():
    # Test already sorted list
    arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    sorted_arr = quick_sort(arr)
    assert sorted_arr == expected

def test_quick_sort_reverse():
    # Test reverse sorted list
    arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    sorted_arr = quick_sort(arr)
    assert sorted_arr == expected

def test_quick_sort_duplicates():
    # Test list with duplicates
    arr = [3, 1, 4, 2, 2, 5, 5]
    expected = [1, 2, 2, 3, 4, 5, 5]
    sorted_arr = quick_sort(arr)
    assert sorted_arr == expected

def test_quick_sort_single_order():
    # Test single out of order list
    arr = [1, 6, 3, 4, 5, 7, 8, 9]
    expected = [1, 3, 4, 5, 6, 7, 8, 9]
    sorted_arr = quick_sort(arr)
    assert sorted_arr == expected

def test_quick_sort_identical():
    # Test near identical
    arr = [2, 2, 2, 2, 2, 2, 2, 1]
    expected = [1, 2, 2, 2, 2, 2, 2, 2]
    sorted_arr = quick_sort(arr)
    assert sorted_arr == expected

def test_counting_sort_empty():
    # Test empty list
    arr = []
    expected = []
    sorted_arr = counting_sort(arr)
    assert sorted_arr == expected

def test_counting_sort_single():
    # Test single element list
    arr = [1]
    expected = [1]
    sorted_arr = counting_sort(arr)
    assert sorted_arr == expected

def test_counting_sort_sorted():
    # Test already sorted list
    arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    sorted_arr = counting_sort(arr)
    assert sorted_arr == expected

def test_counting_sort_reverse():
    # Test reverse sorted list
    arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    sorted_arr = counting_sort(arr)
    assert sorted_arr == expected

def test_counting_sort_duplicates():
    # Test list with duplicates
    arr = [3, 1, 4, 2, 2, 5, 5]
    expected = [1, 2, 2, 3, 4, 5, 5]
    sorted_arr = counting_sort(arr)
    assert sorted_arr == expected

def test_counting_sort_single_order():
    # Test single out of order list
    arr = [1, 6, 3, 4, 5, 7, 8, 9]
    expected = [1, 3, 4, 5, 6, 7, 8, 9]
    sorted_arr = counting_sort(arr)
    assert sorted_arr == expected

def test_counting_sort_identical():
    # Test near identical
    arr = [2, 2, 2, 2, 2, 2, 2, 1]
    expected = [1, 2, 2, 2, 2, 2, 2, 2]
    sorted_arr = counting_sort(arr)
    assert sorted_arr == expected