def removeDuplicate(s):
    s1 = []
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            s1.append(char)

    print("".join(s1))

removeDuplicate("tree traversal")