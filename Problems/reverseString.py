def rev_str(inp_str):

    length = len(inp_str)

    if length == 1:
        return inp_str

    else:
        return inp_str[length - 1] + rev_str(inp_str[:length - 1])

print(rev_str("Rishabh"))
