def larg_cont_sum(arr):
    if len(arr) == 0:
        return 0

    max_Sum = current_Sum = arr[0]
    for num in arr[1:]:
        current_Sum = max(current_Sum + num, num)
        max_Sum = max(current_Sum, max_Sum)
    return max_Sum

result = larg_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])
print(result)