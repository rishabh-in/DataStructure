## Half Pyramid
def half_pyramid(n):
    i = 1
    while i <= n:
        print(i * "*")
        i += 1


half_pyramid(5)

print()


## Inverted half pyramid

def inverted_pyramid(n):
    i = n
    while i > 0:
        print(i * "*")
        i -= 1


inverted_pyramid(5)

print()


## Full pyramid star pattern

def full_pyramid(n):
    ## no of spaces
    k = n * 2 - 2

    ## This is outer loop for rows
    for i in range(n):

        ## This inner loop is for spaces
        for j in range(0, k):
            print(end=" ")
        k -= 1

        ## This inner loop is for column and print start after space
        for j in range(0, i + 1):
            print("* ", end="")

        print()


full_pyramid(3)

print()


## 180 degree rotated pyramid

def pyramid_180(n):
    spaces = n * 2 - 2
    for i in range(n):
        for j in range(0, spaces):
            print(end=" ")
        spaces -= 2

        for j in range(0, i + 1):
            print("* ", end="")
        print()


pyramid_180(4)

print()


## Number pattern

def numPat(n):
    for i in range(1, n + 1):
        k = 1
        while k <= i:
            print(k, end=" ")
            k += 1
        print()


numPat(4)

print()


## Inverted number

def inverted_num(n):
    for i in range(1, n + 1):
        k = 1
        for j in range(i, n + 1):
            print(k, end=" ")
            k += 1
        print()


inverted_num(5)

print()


## without reassigning

def noReassignment(n):
    k = 1
    for i in range(0, n):
        for j in range(0, i+1):
            print(k, end=" ")
            k = k + 1
        print()


noReassignment(5)

print()


## Pyramid using alphabets (same alpha)

def alpha_pyramid(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            print(chr(num), end=" ")
        num += 1
        print()

alpha_pyramid(4)

print()
## Alpha pyramid different alphabets

def alpha_pyramid2(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i + 1):
            print(chr(num), end=" ")
            num += 1
        print()


alpha_pyramid2(4)