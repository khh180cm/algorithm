"""
추상적 자료구조로 LinkedList 라는 이름의 클래스가 정의되어 있다고 가정하고,
이 리스트를 처음부터 끝까지 순회하는 메서드 traverse() 를 완성하세요.

메서드 traverse() 는 리스트를 리턴하되,
이 리스트에는 연결 리스트의 노드들에 들어 있는 데이터 아이템들을 연결 리스트에서의 순서와 같도록 포함합니다.
예를 들어, LinkedList L 에 들어 있는 노드들이 43 -> 85 -> 62 라면, 올바른 리턴 값은 [43, 85, 62] 입니다.

이 규칙을 적용하면, 빈 연결 리스트에 대한 순회 결과로 traverse() 메서드가 리턴해야 할 올바른 결과는 [] 입니다.
"""

import unittest
from typing import List


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0

    def traverse(self) -> List:
        res = []
        cur = self.head
        while cur:
            res.append(cur.data)
            cur = cur.next
        return res


class 연결리스트_순회_테스트(unittest.TestCase):
    def test_빈_연결리스트는_빈_배열을_리턴한다(self):
        linked_list = LinkedList()
        actual = linked_list.traverse()
        expected = []

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
