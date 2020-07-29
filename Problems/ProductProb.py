def integer_prod(arr):
    output = [None] * len(arr)
    product = 1
    i = 0

    while i < len(arr):             ## 1st pass for product of items before the current integer
        output[i] = product
        product *= arr[i]
        i += 1

    product = 1
    i = len(arr) - 1

    while i >= 0:                   ## 2nd pass for the product of items after the current integer

        output[i] *= product
        product *= arr[i]
        i -= 1
    return output

lst = [1, 2, 3, 4]
print(integer_prod(lst))