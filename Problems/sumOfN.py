def sumOfN(n):
    return n*(n+1)//2


t = int(input("Enter no of test cases:"))
while t:
    n = int(input("Enter N:"))
    print(sumOfN(n))
    t = t - 1