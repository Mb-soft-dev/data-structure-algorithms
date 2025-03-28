from typing import List


def binarySearch(arr: List[int], value: int) -> int:
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def binarySearchRec(arr: List[int], value: int) -> int:
    if len(arr) == 0:
        return -1  # Base case

    mid = len(arr) // 2  # Find the middle index

    if arr[mid] == value:
        return mid
    # If the value is smaller than the middle element, search the left half
    elif arr[mid] > value:
        result = binarySearchRec(arr[:mid], value)
        return result if result == -1 else mid - len(arr[:mid]) + result
    # If the value is larger than the middle element, search the right half
    else:
        result = binarySearchRec(arr[mid + 1 :], value)
        return mid + 1 + result if result != -1 else -1
