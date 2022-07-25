"""
선형탐색
- O(N)
"""
from typing import List

L = [3, 8, 1, 5, 2, 6, 9]


def linear_search(target: int, rand_list: List) -> int:
    found = -1
    for i in rand_list:
        if i == target:
            found = i
            break
    return found


res = linear_search(6, L)
print(res)
