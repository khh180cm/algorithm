"""
이진탐색
"""


L = [1, 3, 7, 8, 12, 15, 17, 21, 24, 30, 32, 34, 39, 45, 51, 62]
num = 31


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle - 1
        else:
            break
    else:
        return -1
    return 1


res = binary_search(L, num)
print(res)
