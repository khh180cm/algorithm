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


linked_list = LinkedList(5)
linked_list.append(12)
first_node = linked_list.get_node(0)  # -> 5를 들고 있는 노드를 반환해야 합니다!
print(first_node.data)

second_node = linked_list.get_node(1)  # -> 5를 들고 있는 노드를 반환해야 합니다!
print(second_node.data)
