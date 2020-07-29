def insertionSort(arr):

    for i in range(1, len(arr)):
        currentValue = arr[i]
        position = i
        while position > 0 and arr[position - 1] > currentValue:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = currentValue
    print(arr)

arr = [4,1,6,9,56,34,87,23,7,3]
insertionSort(arr)