## getting a list of all divisor of a number

## approach 1- traverse through a range up to the number and check whether its divisible or not O(n)
## approach 2 - T.C - O(root(n))
from math import sqrt

def approach1(n):
    divList1 = []
    for i in range(1, n+1):
        if n % i == 0:
            divList1.append(i)
    return divList1

def approach2(n):
    div2 = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            div2.add(i)
            div2.add(n//i)
    return list(div2)

print(approach1(24))
print(approach2(24))
