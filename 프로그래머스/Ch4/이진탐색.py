"""
문제 설명
리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어지고,
또한 탐색의 대상이 되는 리스트 내에서의 범위 인덱스가 l 부터 u 까지로 (인자로) 정해질 때,
x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요.
만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다.
리스트 L 은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다.
또한, 동일한 원소는 두 번 이상 나타나지 않습니다.

인덱스 범위를 나타내는 l 과 u 가 인자로 주어지는 이유는, 이 함수를 재귀적인 방법으로 구현하기 위함입니다.
"""

import unittest
from typing import List


def binsearch(L: List, target: int, left: int, right: int) -> int:
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if L[mid] < target:
            left = mid + 1
        elif L[mid] > target:
            right = mid - 1
        else:
            return mid
        return binsearch(L, target, left, right)


class 해가_존재하는_이진탐색(unittest.TestCase):
    def test_타켓_2가_첫_번째_인덱스이므로_0을_리턴해야_한다(self):
        L = [2, 3, 5, 6, 9, 11, 15]
        target = 2
        left = 0
        right = len(L) - 1

        answer = 0
        self.assertEqual(binsearch(L, target, left, right), answer)

    def test_타켓_15가_마지막에_있으므로_인덱스_6을_리턴해야_한다(self):
        L = [2, 3, 5, 6, 9, 11, 15]
        target = 15
        left = 0
        right = len(L) - 1

        answer = 6
        self.assertEqual(binsearch(L, target, left, right), answer)

    def test_타켓_3이_두_번째_인덱스이므로_1을_리턴해야_한다(self):
        L = [2, 3, 5, 6, 9, 11, 15]
        target = 3
        left = 0
        right = len(L) - 1

        answer = 1
        self.assertEqual(binsearch(L, target, left, right), answer)

    def test_타켓_15가_마지막에_있으므로_인덱스_6을_리턴해야_한다(self):
        L = [2, 3, 5, 6, 9, 11, 15]
        target = 15
        left = 0
        right = len(L) - 1

        answer = 6
        self.assertEqual(binsearch(L, target, left, right), answer)


class 해가_존재하지_않는_이진탐색(unittest.TestCase):
    def test_타켓_minus_100은_리스트에_없으므로_minus_1을_리턴해야_한다(self):
        L = [2, 3, 5, 6, 9, 11, 15]
        target = -100
        left = 0
        right = len(L) - 1

        answer = -1
        self.assertEqual(binsearch(L, target, left, right), answer)

    def test_타켓_7은_리스트에_없으므로_minus_1을_리턴해야_한다(self):
        L = [2, 3, 5, 6, 9, 11, 15]
        target = 7
        left = 0
        right = len(L) - 1

        answer = -1
        self.assertEqual(binsearch(L, target, left, right), answer)

    def test_타켓_100은_리스트에_없으므로_minus_1을_리턴해야_한다(self):
        L = [2, 3, 5, 6, 9, 11, 15]
        target = 100
        left = 0
        right = len(L) - 1

        answer = -1
        self.assertEqual(binsearch(L, target, left, right), answer)


if __name__ == "__main__":
    unittest.main()
