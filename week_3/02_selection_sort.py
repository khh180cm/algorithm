"""
선택 정렬(오름차순)
"""
input = [4, 6, 2, 9, 1]


# 방법 1
def selection_sort_1(array):
    n = len(array)
    for i in range(n-1):
        min_idx = i
        for j in range(n-i):
            if array[min_idx] > array[i+j]:
                min_idx = i + j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


selection_sort_1(input)
print(input)


# 방법 2
def selection_sort_2(array):
    n = len(array)
    for i in range(n-1):  # 0, 1, 2, 3, 4
        min_idx = i
        for j in range(n-i):
            if array[min_idx] > array[i+j]:
                array[min_idx], array[i+j] = array[i+j], array[min_idx]
    return array


selection_sort_2(input)
print(input)


# 방법 3
def selection_sort_3(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


selection_sort_3(input)
print(input)
