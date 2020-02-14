from math import floor


## implements recursive binary search for an array list
# @param: arr: the array where to search x
# @param: left: the first index of the array
# @param: right: the last index of the array
# @param: x: the value that as to be searched
# @returns: the index where x has been found, or where it should be inserted to keep ordering
def binary_search_rec(arr, left, right, x):
    if (right - left) < 1:
        if x <= arr[left]:
            return left
        else:
            return left + 1
    else:
        mid = floor((left + right) / 2)
        if x > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
        return binary_search_rec(arr, left, right, x)

## implements binary search for an array list
# @param: arr: the array where to search x
# @param: x: the value that as to be searched
# @returns: the index where x has been found, or where it should be inserted to keep ordering
def binary_search(arr, x):
    return binary_search_rec(arr, 0, len(arr) - 1, x)
