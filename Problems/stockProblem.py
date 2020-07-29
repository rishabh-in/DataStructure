def max_profit(arr):
    own_stock = arr[0]
    profit = 0

    for i in range(1, len(arr)):
        if arr[i] < own_stock :
            own_stock = arr[i]

        else:
            new_profit = arr[i] - own_stock

            if new_profit > profit:
                profit = new_profit

    return  profit

arr = [12, 11, 15, 3, 10, 2, 15, 1, 7, 20]
print(max_profit(arr))