def word_split(str,lst, output = None):
    if output is None:
        output = []

    if lst[0] in str:
        output.append(lst[0])
        lst.remove(lst[0])
        return word_split(str, lst, output)


print(word_split("rishabhnamemy",["rishabh","is","my","name"]))