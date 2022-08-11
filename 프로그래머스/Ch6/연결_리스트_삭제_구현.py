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


class 연결리스트_삭제_테스트(unittest.TestCase):
    def test_빈_연결리스트는_삭제_기능이_불가하다(self):
        linked_list = LinkedList()

        with self.assertRaises(IndexError):
            linked_list.pop(1)
            linked_list.pop(2)
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_노드_하나인_연결_리스트에서_삭제가_가능하다(self):
        node = Node(5)
        linked_list = LinkedList()
        linked_list.insert(1, node)

        res = linked_list.pop(1)

        self.assertEqual(res, 5)
        self.assertEqual(linked_list.node_cnt, 0)
        self.assertEqual(linked_list.traverse(), [])
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_노드_3개인_연결_리스트에서_중간_노드를_삭제한다(self):
        node_list = [Node(i) for i in [5, 6, 7]]
        linked_list = LinkedList()
        for i in range(len(node_list)):
            linked_list.insert(i + 1, node_list[i])

        res = linked_list.pop(2)

        self.assertEqual(res, 6)
        self.assertEqual(linked_list.node_cnt, 2)
        self.assertEqual(linked_list.traverse(), [5, 7])
        self.assertEqual(linked_list.head.data, 5)
        self.assertEqual(linked_list.tail.data, 7)

    def test_노드_5개인_연결_리스트에서_마지막_노드를_삭제한다(self):
        node_list = [Node(i) for i in [5, 6, 7, 8, 9]]
        linked_list = LinkedList()
        for i in range(len(node_list)):
            linked_list.insert(i + 1, node_list[i])

        res = linked_list.pop(5)

        self.assertEqual(res, 9)
        self.assertEqual(linked_list.node_cnt, 4)
        self.assertEqual(linked_list.traverse(), [5, 6, 7, 8])
        self.assertEqual(linked_list.head.data, 5)
        self.assertEqual(linked_list.tail.data, 8)


if __name__ == "__main__":
    unittest.main()
