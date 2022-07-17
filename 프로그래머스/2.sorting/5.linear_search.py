"""
선형탐색
"""

L = [3, 8, 2, 7, 6, 10, 9]
num = 6


def linear_search(arr, target):
    i = 0
    while i < len(arr) and arr[i] != target:
        i += 1
    if i < len(arr):
        return i
    else:
        return -1


res1 = linear_search(L, num)
res2 = linear_search(L, 100000)
print(res1)
print(res2)
