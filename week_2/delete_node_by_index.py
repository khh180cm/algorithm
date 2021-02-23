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

    def delete_node(self, index):
        if index == 0:
            # 헤드 변경 방법 1
            self.head = self.head.next
            # 헤드 변경 방법 2
            # cur_first_node = self.head
            # self.head = cur_first_node.next
            return
        prev_node = self.get_node(index-1)
        prev_node.next = prev_node.next.next


linked_list = LinkedList(5)
linked_list.append(7)
linked_list.append(9)
linked_list.append(11)

linked_list.delete_node(0)
linked_list.print_all()
