def str_com(inp_str):
    final_str = ""
    dict = {}

    for val in inp_str:
        if val in dict:
            dict[val] += 1
        else:
            dict[val] = 1

    for key, val in dict.items():
        final_str = final_str + key + str(val)

    print(final_str)


def compress(s):
    final_str = ""
    length = len(s)
    if length == 0:
        return ""
    if length == 1:
        return s + "1"

    count = 1
    i = 1
    while i < length:
        if s[i] == s[i-1]:
            count += 1
        else:
            final_str = final_str + s[i-1] + str(count)
            count = 1
        i += 1

    final_str = final_str + s[i-1] + str(count)
    return final_str

print(compress("AAR"))
str_com("AAB")