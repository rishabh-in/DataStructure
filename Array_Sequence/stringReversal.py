def rev_word(s):
    s1 = s.strip()
    s1 = s1.split()
    ## print(s1[::-1])   ## we can use reverse function
    s1 = reversed(s1)
    s1 = " ".join(s1)
    print(s1)

def rev_word2(s):
    word = []
    length = len(s)
    spaces = [" "]

    i = 0
    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            word.append(s[word_start:i])
        i += 1

    word = reversed(word)
    return " ".join(word)


print(rev_word2("     My name is Rishabh       "))
rev_word("     My name is Rishabh       ")