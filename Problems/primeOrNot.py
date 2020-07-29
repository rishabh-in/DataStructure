from math import sqrt
def prime1(n):          ## O(n)
    divCount = 0
    for i in range(1, n+1):
        if n % i == 0:
            divCount += 1
    if divCount == 2:
        return True
    return False

def prime2(n):               ## O(root(n))
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(sqrt(n)) + 1):
        if n % i == 0 or n % (i+2):
            return False
    return True

print(prime1(7))
print(prime2(30))