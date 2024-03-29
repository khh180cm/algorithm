from audioop import reverse
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

    def __repr__(self):
        if self.node_cnt == 0:
            return f"Empty LinkedList"
        else:
            res = self.traverse()
            parsed = "->".join([str(i) for i in res])
            return f"LinkedList: {parsed}"

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
            if self.node_cnt != 0:
                node.next = self.head
                self.head = node
            else:
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

    def pop(self, pos: int) -> int:
        if self.node_cnt == 0:
            raise IndexError
        elif self.node_cnt == 1:
            res = self.head
            self.head = None
            self.tail = None
        elif pos < self.node_cnt:
            prev = self.head
            for i in range(pos - 2):
                prev = prev.next
            res = prev.next
            prev.next = prev.next.next
        else:
            last = self.head
            for i in range(pos - 2):
                last = last.next
            res = self.tail
            last.next = None
            self.tail = last
        self.node_cnt -= 1
        return res.data


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
        linked_list.insert(3, node)

        node = Node(8)
        res = linked_list.insert(5, node)

        self.assertFalse(res)
        self.assertEqual(linked_list.traverse(), [5, 6, 7])

    def test_연결_리스트의_첫_번째_위치로_연속해서_삽입이_가능하다(self):
        linked_list = LinkedList()
        node_list = [Node(i) for i in range(5)]
        for node in node_list:
            res = linked_list.insert(1, node)
            self.assertTrue(res)
        self.assertEqual(linked_list.node_cnt, 5)
        self.assertEqual(
            linked_list.traverse(),
            sorted([i for i in range(5)], reverse=True),
        )


if __name__ == "__main__":
    unittest.main()
