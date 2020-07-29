## My solution (O(n^2)

def pair_sum(arr, k):
    finalLst = []
    lst = []
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                lst.append(arr[i])
                lst.append(arr[j])
                finalLst.append(lst)
                lst = []
            else:
                continue
    print(finalLst)
    print(len(finalLst))

pair_sum([1,3,2,2], 4)




## Good solution is using sets and change the complexity to linear O(n)

def pair__sum(arr, k):
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target in seen:
            output.add((min(num, target), max(num, target)))
        else:
            seen.add(num)

    output = list(output)
    print("\n".join(map(str, output)))
    print(len(output))

pair__sum([1,3,2,2], 4)