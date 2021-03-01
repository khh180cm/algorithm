"""
버블 정렬(오름차순)
"""

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


bubble_sort(input)
print(input)
