"""
삽입 정렬
"""
input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(input)
    for i in range(1, n):
        compare_idx = i
        for j in range(i):
            if array[j] > array[compare_idx]:
                array[j], array[compare_idx] = array[compare_idx], array[j]
            else:
                break
    return array


insertion_sort(input)
print(input)
