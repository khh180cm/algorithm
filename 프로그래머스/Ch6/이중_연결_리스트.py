class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.node_cnt = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def traverse(self):
        cur = self.head.next
        result = []
        while cur.next:
            result.append(cur.data)
        return result

    def reverse(self):
        cur = self.tail.prev
        result = []
        while cur.prev:
            result.append(cur.data)
        return result

    def insert_after(self, prev: Node, new_node: Node) -> bool:
        next = prev.next
        new_node.prev = prev
        new_node.next = next
        prev.next = new_node
        next.prev = new_node
        self.node_cnt += 1
        return True

    def get_at(self, pos: int) -> Node:
        if pos < 1 or pos > self.node_cnt + 1:
            raise IndexError

        if pos > self.node_cnt // 2:
            cur = self.tail
            for _ in range(self.node_cnt - pos + 1):
                cur = cur.prev
        else:
            cur = self.head
            for _ in range(pos):
                cur = cur.next
        return cur

    def insert_at(self, pos: int, new_node: Node) -> bool:
        prev = self.get_at(pos - 1)
        return self.insert_after(prev, new_node)
