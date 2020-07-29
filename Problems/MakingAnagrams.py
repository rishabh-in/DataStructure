def anagram(a, b):
    dict = {}

    for ele in a:
        if ele not in dict:
            dict[ele] = 1
        else:
            dict[ele] += 1
    count = 0
    for ele in b:
        if ele not in dict:
            count += 1
        else:
            dict[ele] -= 1

    print(dict)
    for k in dict:
        if dict[k] != 0:
            count = count + abs(dict[k])
    return count


print(anagram("abc", "cde"))