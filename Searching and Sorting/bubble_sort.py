def bubble_sort(arr):
    n = len(arr)

    for i in range(n):              ## for steps
        for j in range(0, n - i - 1):  ## for iteration
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]

    print(arr)

bubble_sort([4,6,3,9,1])