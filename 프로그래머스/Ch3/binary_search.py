"""
이진 탐색
- 시간복잡도: log(N)
"""

from typing import List

L = [1, 3, 7, 8, 12, 15, 17, 21, 24, 30, 32, 34, 39, 45, 51, 62]
TARGET = 62


def binary_search(num_list: List, target: int) -> int:
    left = 0
    right = len(num_list) - 1
    idx = -1
    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] < target:
            left = mid + 1
        elif num_list[mid] > target:
            right = mid - 1
        else:
            idx = mid
            break
    return idx


res = binary_search(L, TARGET)
print(res)
