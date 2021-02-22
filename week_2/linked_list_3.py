# 유저 주소 정보

class Node:
    def __init__(self, address):
        self.address = address
        self.next = None


class LinkedList:
    def __init__(self, address):
        self.head = Node(address)

    def append(self, address):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(address)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.address)
            cur = cur.next


a = LinkedList("강남구 도곡로")
a.append("강남구 역삼동")
a.append("서울시 관악구")

a.print_all()
