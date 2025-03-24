from typing import List
import pytest
from algorithms.quickSort  import quickSortRec


def test_quickSort():
    arr = [3,8, 4, 2, 10] 
    expected = sorted(arr)
    result = quickSortRec(arr)

    assert result == expected, f"Expected {expected}, but got {result}"
    print(result, "✅ Array sorted correctly")
