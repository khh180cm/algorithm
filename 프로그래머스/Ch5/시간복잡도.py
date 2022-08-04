"""
삽입정렬의 시간복잡도: O(n^2)
"""
import unittest
from typing import List


def insertion_sorting(L: List) -> List:
    length = len(L)
    if length <= 1:
        return L
    for i in range(length):
        for j in range(i + 1):
            if i == j:
                break
            elif L[j] > L[i]:
                L[i], L[j] = L[j], L[i]
    return L


class 삽입정렬_테스트(unittest.TestCase):
    def test_빈_리스트는_빈_리스트를_리턴한다(self):
        L = []

        res = insertion_sorting(L)

        self.assertEqual(L, res)

    def test_원소가_한_개인_리스트는_그대로_리턴된다(self):
        L = [100]

        res = insertion_sorting(L)

        self.assertEqual(L, res)

    def test_음수가_포함된_정렬된_리스트도_정렬된다(self):
        L = [-10, 5, 15]

        res = insertion_sorting(L)

        self.assertEqual(res, sorted(L))

    def test_음수가_포함된_정렬되지_않은_리스트도_정렬된다(self):
        L = [5, 0, -15, -10]

        res = insertion_sorting(L)

        self.assertEqual(res, sorted(L))

    def test_음수로_이뤄진_리스트도_정렬된다(self):
        L = [-99, -3443, -33, -1213]

        res = insertion_sorting(L)

        self.assertEqual(res, sorted(L))

    def test_음수와_영_그리고_양수로_이뤄진_리스트도_정렬된다(self):
        L = [-99, -3443, -33, -1213, 324, 33, 111, 333, 333, 0, 777]

        res = insertion_sorting(L)

        self.assertEqual(res, sorted(L))

    def test_동일한_수로_구성된_리스트도_정렬된다(self):
        L = [1 for _ in range(9)]

        res = insertion_sorting(L)

        self.assertEqual(res, sorted(L))


if __name__ == "__main__":
    unittest.main()
