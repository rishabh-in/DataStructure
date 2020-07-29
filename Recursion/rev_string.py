
'''

def rev_str(string, n=None):
    if n is None:
        n = len(string)
    if n <= 1:
        return s[n - 1]
    elif n > 1:
        return s[n - 1] + str(rev_str(s, n - 1))

s = "Rishabh Tiwari"
print(rev_str(s, len(s)))

'''

## Without passing the size of string

def rev_str2(s):

    l = len(s)

    ## base case

    if l == 1:
        return s

    ## recursion
    else:
        return s[l - 1] + str(rev_str2(s[0:l-1]))

print(rev_str2("My name is Rishabh Tiwari"))