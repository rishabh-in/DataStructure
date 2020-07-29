def int_sum(n):
    if n == 0:
        return 0
    else:
        return n + int_sum(n-1)

print(int_sum(5))

###       sum of each integer in string of integer

def int_sum2(n):
     rem = n%10
     n = n//10

     if n == 0:
         return rem
     else:
         return rem + int_sum2(n)

print(int_sum2(1234))
print(int_sum2(453627))