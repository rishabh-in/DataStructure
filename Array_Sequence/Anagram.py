def anagram1(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    return sorted(s1) == sorted(s2)

def anagram2(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    count = {}
    for i in s1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for j in s2:
        if j in count:
            count[j] -= 1
        else:
            count[j] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True

print(anagram1("dog", "god"))
print(anagram2("dog", "god"))


