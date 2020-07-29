### For unordered List

def unordered_seq_search(arr,ele):
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found = True
        else:
            pos += 1
    return found


arr1 = [6,5,3,7,3,9,2]
print(unordered_seq_search(arr1 ,5))

##  For ordered list

def ordered_seq_search(arr, ele):
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                return found
            else:
                pos += 1

    return found

arr2 = [1,2,3,4,5,6,7]
print(ordered_seq_search(arr2, 9))