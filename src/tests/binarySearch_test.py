from typing import List
import pytest
from algorithms.binarySearch import binarySearch
from algorithms.binarySearch import binarySearchRec


def test_search():
    arr = list(range(1, 10000001)) 
    index = binarySearch(arr, 2)
    assert index == 1

def test_search_not_found():
    arr = list(range(1, 101)) 
    index = binarySearch(arr, 200)
    assert index == - 1

def test_search_rec(): 
    arr = list(range(1, 7))
    index = binarySearchRec(arr, 2)
    assert index == 1
