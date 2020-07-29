## My solution - Time complexity is O(3n)
def missing_element(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    dict = {}

    for val in arr1:
        if val in dict:
            dict[val] += 1
        else:
            dict[val] = 1

    for val in arr2:
        if val in dict:
            dict[val] -= 1
        else:
            dict[val] = 1

    for ele in dict:
        if dict[ele] != 0:
            print(str(ele) + " is missing here.")


missing_element([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
missing_element([5, 5, 7, 7], [5, 7, 7])


## Another solution Good O(NlogN)

def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return "None"

print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
print(finder([5, 5, 7, 7], [5, 5, 7, 7]))

## Another way of doing this is using default dict, we will get linear time complexity

import collections

def finder2(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num

        else:
            d[num] -= 1


print(finder2([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
print(finder2([5, 5, 7, 7], [5, 5, 7]))