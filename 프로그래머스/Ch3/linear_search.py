"""
선형 탐색
- 시간복잡도: O(N)
"""
from typing import List

L = [3, 8, 1, 5, 2, 6, 9]
TARGET = 6


def linear_search(rand_list: List, target: int) -> int:
    found = -1
    for idx, val in enumerate(rand_list):
        if val == target:
            found = idx
            break
    return found


res = linear_search(L, TARGET)
print(res)


"""
선형 탐색을 리스트의 내장함수(index)로 구하기
- 시간복잡도: O(N)
"""


def linear_search_by_index(rand_list: List, target: int) -> int:
    try:
        return rand_list.index(target)
    except ValueError:
        return -1


res = linear_search(L, TARGET)
print(res)
