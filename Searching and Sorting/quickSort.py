def quickSort(arr):
    quickSort_help(arr, 0, len(arr) - 1)
    print(arr)
    
def quickSort_help(arr, first, last):
    if first < last:
        
        splitPoint = partition(arr, first, last)
        quickSort_help(arr, first, splitPoint - 1)
        quickSort_help(arr, splitPoint + 1, last)

def partition(arr, first, last):
    pivot = arr[first]
    leftMark = first + 1
    rightMark = last
    done = False
    
    while not done:
        while leftMark <= rightMark and arr[leftMark] <= pivot:
            leftMark += 1
            
        while rightMark >= leftMark and arr[rightMark] >= pivot:
            rightMark -= 1
            
        if rightMark < leftMark:
            done = True
        else:
            temp = arr[leftMark]
            arr[leftMark] = arr[rightMark]
            arr[rightMark] = temp
    
    temp = arr[first]
    arr[first] = arr[rightMark]
    arr[rightMark] = temp
    
    return rightMark

arr = [4, 1, 6, 9, 56, 34, 87, 23, 7, 3]
quickSort(arr)