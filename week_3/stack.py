"""
스택 자료구조 구현
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        new_head = self.head.next
        pop_data = self.head.data
        self.head = new_head
        return pop_data

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        cur_node = self.head
        return cur_node.data

    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(0)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.pop())
print(stack.pop())
