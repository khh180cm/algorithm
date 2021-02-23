class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cnt = 0
        cur_node = self.head
        while cur_node:
            if index == cnt:
                return cur_node
            else:
                cur_node = cur_node.next
                cnt += 1

    def add_node(self, index, data):
        # 방법 1
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        nth_node = self.get_node(index)
        prev_node = self.get_node(index-1)
        prev_node.next = new_node
        new_node.next = nth_node

        # 방법 2
        # prev_node = self.head
        # next_node = self.head.next
        # cnt = 0
        # while next_node:
        #     prev_node = next_node
        #     next_node = prev_node.next
        #     cnt += 1
        # new_node = Node(data)
        # prev_node.next = new_node
        # new_node.next = next_node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

linked_list.add_node(0, 6)
linked_list.print_all()
