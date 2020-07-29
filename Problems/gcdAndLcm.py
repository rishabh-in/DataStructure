## Euclid algorithm

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def lcm(a, b):
    prod = a*b
    hcf = gcd(a, b)
    Lcm = prod//hcf
    return Lcm

t = int(input("Enter No of test cases: "))

while t:
    a, b = map(int, input("Enter value of a and b:").split())
    print("HCF is {}".format(gcd(a, b)))
    print("LCM is {}".format(lcm(a, b)))
    t = t - 1