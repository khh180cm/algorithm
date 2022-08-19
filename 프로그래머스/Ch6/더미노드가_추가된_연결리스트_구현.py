class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.node_count = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def traverse(self):
        cur = self.head
        res = []
        while cur.next:
            res.append(cur.data)
            cur = cur.next
        return res

    def get_at(self, pos: int) -> Node:
        if pos < 0 or pos > self.node_count:
            return None
        cur = self.head
        for i in range(pos):
            cur = cur.next
        return cur

    def insert_after(self, prev: Node, new_node: Node) -> bool:
        new_node.next = prev.next
        prev.next = new_node
        if prev.next is None:
            self.tail = new_node
        self.node_count += 1
        return True

    def insert_at(self, pos: int, new_node: Node) -> bool:
        if pos < 1 or pos > self.node_count + 1:
            return False

        if pos != 1 and pos == self.node_count + 1:
            prev = self.tail
        else:
            prev = self.get_at(pos - 1)
        return self.insert_after(prev, new_node)

    def pop_after(self, prev: Node) -> Node:
        if prev.next is None:
            return None
        if prev.next == self.tail:
            cur = prev.next
            self.tail = prev
        else:
            cur = prev.next
            prev.next = cur.next
        self.node_count -= 1
        return cur
