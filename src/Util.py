from math import floor


# Returns index of x in arr
def binary_search_rec(arr, l, r, x):
    if (r - l) < 1:
        if x <= arr[l]:
            return l
        else:
            return l+1
    else:
        mid = floor((l + r) / 2)
        if x > arr[mid]:
            l = mid + 1
            return binary_search_rec(arr, l, r, x)

        else:
            r = mid - 1
            return binary_search_rec(arr, l, r, x)


def binary_search(arr, x):
    return binary_search_rec(arr, 0, len(arr) - 1, x)

x = [1,2,3,4,5,6]

binary_search(x,5) 