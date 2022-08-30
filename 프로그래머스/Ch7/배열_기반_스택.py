from mimetypes import init
from Ch6.이중_연결_리스트 import Node, DoublyLinkedList


class ArrayStack:
    def __init__(self) -> None:
        self.data = []

    def size(self) -> int:
        return len(self.data)

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, item) -> None:
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


class LinkedListStack:
    def __init__(self) -> None:
        self.stack = DoublyLinkedList()

    def size(self) -> int:
        return self.stack.node_cnt

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, item):
        new_node = Node(item)
        last_idx = self.size()
        next_idx = last_idx + 1
        self.stack.insert_at(next_idx, new_node)

    def peek(self) -> int:
        last_idx = self.size()
        return self.stack.get_at(last_idx).data
