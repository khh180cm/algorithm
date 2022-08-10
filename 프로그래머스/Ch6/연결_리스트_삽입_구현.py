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
        self.node_cnt = 0

    def traverse(self) -> List:
        res = []
        cur = self.head
        while cur:
            res.append(cur.data)
            cur = cur.next
        return res

    def insert(self, pos: int, node: Node) -> bool:
        if self.node_cnt + 1 < pos:
            return False
        elif self.node_cnt == 0:
            self.head = node
            self.tail = node
        elif pos == 1:
            self.head = node
            self.tail = node
        elif 1 < pos < self.node_cnt + 1:
            prev = self.head
            for i in range(pos - 2):
                prev = prev.next
            node.next = prev
            prev.next = node
        else:
            prev_tail = self.tail
            prev_tail.next = node
            self.tail = node
        self.node_cnt += 1
        return True


class 연결리스트_삽입_테스트(unittest.TestCase):
    def test_빈_연결리스트에_단일_노드를_삽입한다(self):
        node = Node(5)
        linked_list = LinkedList()
        res = linked_list.insert(1, node)

        self.assertTrue(res)
        self.assertEqual(linked_list.traverse(), [5])

    def test_빈_연결리스트에_순차적으로_노드를_삽입한다(self):
        node = Node(5)
        linked_list = LinkedList()
        res1 = linked_list.insert(1, node)
        node = Node(3)
        res2 = linked_list.insert(2, node)

        self.assertTrue(res1)
        self.assertTrue(res2)
        self.assertEqual(linked_list.traverse(), [5, 3])

    def test_빈_연결_리스트_길이를_초과하는_삽입은_불가하다(self):
        node = Node(5)
        linked_list = LinkedList()
        print(linked_list.node_cnt)
        res = linked_list.insert(2, node)

        self.assertFalse(res)
        self.assertEqual(linked_list.traverse(), [])

    def test_연결_리스트_길이를_초과하는_삽입은_불가하다(self):
        linked_list = LinkedList()
        node = Node(5)
        linked_list.insert(1, node)
        node = Node(6)
        linked_list.insert(2, node)

        node = Node(7)
        res = linked_list.insert(5, node)

        self.assertFalse(res)
        self.assertEqual(linked_list.traverse(), [5, 6])


if __name__ == "__main__":
    unittest.main()
