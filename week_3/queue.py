class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        if self.is_empty():
            new_node = Node(value)
            self.tail = new_node
            self.head = self.tail
        else:
            last_node = self.tail
            new_node = Node(value)
            last_node.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        deleted_head = self.head
        self.head = self.head.next
        return deleted_head.data

    def peek(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.head.data

    def is_empty(self):
        return self.head is None


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
res = queue.peek()
print(res)
queue.dequeue()
res = queue.peek()
print(res)
res = queue.peek()
print(res)
queue.dequeue()
res = queue.peek()
print(res)
