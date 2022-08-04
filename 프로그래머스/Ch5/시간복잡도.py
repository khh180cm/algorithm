"""
삽입정렬의 시간복잡도: O(n^2)
"""
from typing import List


L = [54, 26, 93, 17, 77, 31, 43, 55, 20]


def insertion_sorting(L: List) -> List:
    length = len(L)
    for i in range(length):
        for j in range(i + 1):
            print(i, j)
            if i == j:
                break
            elif L[j] > L[i]:
                L[i], L[j] = L[j], L[i]
    return L


res = insertion_sorting(L)
print(res)
