## Wrong solution
'''
def balance_check(s):
    parentheses = {
        "(" : ")",
        "{" : "}",
        "[" : "]",
        ")" : "(",
        "}" : "{",
        "]" : "["
    }
    temp_list = []
    for i in s:
        temp_list.append(parentheses[i])

    temp_list = reversed(temp_list)
    temp_list = "".join(temp_list)
    return s == temp_list

print(balance_check("[](){([[[]]])}"))

'''
## Correct solution
def balance_check(s):
    if len(s) % 2 != 0:
        return False

    opening = set("({[")
    matching = set([("(", ")"), ("{", "}"), ("[", "]")])
    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)

        else:
            if len(stack) == 0:
                return False

            else:
                last_open = stack.pop()
                if (last_open, paren) not in matching:
                    return False
    return len(stack) == 0

print(balance_check("(){}[]({})"))