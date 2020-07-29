def str_prm(s):
    out = []

    if len(s) == 1:
        out = [s]
        return out
    else:
        for i, let in enumerate(s):
            for prm in str_prm(s[:i] + s[i+1:]):
                out += [let + prm]
        return out

print(str_prm("abc"))