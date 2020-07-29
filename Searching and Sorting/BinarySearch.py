## Iterative binary search

def itr_binary_search(arr, ele):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:

        mid = (first + last) // 2

        if ele == arr[mid]:
            found = True

        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(itr_binary_search(arr, 11))


## recursive binary search

def rec_binary_search(arr, ele):
    # Base case
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if ele == arr[mid]:
            return True

        if ele < arr[mid]:
            return rec_binary_search(arr[:mid], ele)
        else:
            return rec_binary_search(arr[mid+1:], ele)



print(rec_binary_search(arr, 6))