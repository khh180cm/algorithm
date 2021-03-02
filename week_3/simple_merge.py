array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    idx_a = 0
    idx_b = 0
    len_a = len(array1)
    len_b = len(array2)
    res = []
    while True:
        if array1[idx_a] > array2[idx_b]:
            res.append(array2[idx_b])
            idx_b += 1
        else:
            res.append(array1[idx_a])
            idx_a += 1
        if idx_a == len_a -1 or idx_b == len_b - 1:
            break
    if idx_b == len_b - 1:
        return res + array1[idx_a:]
    else:
        return res + array2[idx_b:]


print(merge(array_a, array_b))
