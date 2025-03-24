
"""
The quickSortRec function is a recursive implementation of the QuickSort algorithm.

QuickSort is an efficient sorting algorithm that follows the divide-and-conquer paradigm. 
It works by selecting a 'pivot' element from the array and partitioning the remaining elements into two sub-arrays: those smaller than the pivot and those greater than the pivot. It then recursively sorts these sub-arrays.

### How to Use:
- Call the `quickSortRec` function, passing in an array of integers that you want to sort.
- The function will return a sorted version of the input array.

### Notes:
- The algorithm's time complexity is O(n log n) on average but can degrade to O(n²) in the worst case if a poor pivot is chosen repeatedly (e.g., when the input array is already sorted).
- This implementation uses the middle-left element as the pivot, which helps in balancing the partitioning.
- The algorithm handles duplicates by placing equal elements in a separate `equal` array, ensuring stability.
"""
from typing import List, Union

def quickSortRec(arr: List[int]) -> List[int]:
    # Base case: If the array has 0 or 1 element, it's already sorted
    if len(arr) < 2:
        return arr

    # Choose a pivot element (here, we take the middle-left element)
    pivot_index = (len(arr) // 2) - 1  
    pivot = arr[pivot_index]

    # Partition the array into three parts:
    less = [num for num in arr if num < pivot]  
    equal = [num for num in arr if num == pivot]
    greater = [num for num in arr if num > pivot] 

    # Recursively sort the smaller and greater partitions, then combine
    return quickSortRec(less) + equal + quickSortRec(greater)
