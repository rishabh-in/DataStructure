def squareRoot(n):

    if n < 0:
        return 0
    else:
        num = n//2 + 1
        for i in range(0, num):
            val = i * i
            if val == n:
                return i
            elif val > n:
                return i - 1
            else:
                continue

print(squareRoot(24))