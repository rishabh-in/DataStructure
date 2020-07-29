def shellSort(arr):
    subListCount = len(arr) // 2

    while subListCount:
        for start in range(subListCount):
            shell_insertionSort(arr, start, subListCount)
        subListCount = subListCount // 2
    print(arr)
def shell_insertionSort(arr, start, gap):

    for i in range(start + gap, len(arr), gap):
        currentValue = arr[i]
        position = i

        while position >= gap and arr[position - gap] > currentValue:
            arr[position] = arr[position - gap]
            position = position - gap

        arr[position] = currentValue



arr = [56,1,6,9,4,34,87,23,7,3]
shellSort(arr)