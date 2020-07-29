def min_max(n):
    smallest = 9
    largest = 0
    while n:
        r = n%10
        largest = max(r, largest)
        smallest = min(r, smallest)
        n = n // 10

    return largest, smallest

def max_pairs(arr):
    bit_array = []

    for ele in arr:
        maxBit, minBit = min_max(ele)
        resultant_bit = maxBit * 11 + minBit * 7

        if resultant_bit / 2 > 50:
            lsb = resultant_bit % 100
            bit_array.append(lsb // 10)

        else:
            bit_array.append(resultant_bit // 10)

    dict = {}
    for i in range(len(bit_array)):
        for j in range(i + 1, len(bit_array)):
            if bit_array[i] == bit_array[j]:
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    if bit_array[i] in dict:
                        dict[bit_array[i]] += 1
                    else:
                        dict[bit_array[i]] = 1
            else:
                continue

    pairs = 0
    for ele in dict:
        if dict[ele] >= 2:
            pairs += 2
        else:
            pairs += 1
    return pairs

n = int(input())
items = list(map(int, input().split()))
print(max_pairs(items))