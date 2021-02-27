"""
링크드 리스트
 - 마지막 노드에서 k 번째 노드 데이터 출력하기
"""


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

    def get_total_num_of_nodes(self):
        """
        연결 리스트 노드의 총 개수
        :return: int(노드 총 개수)
        """

        cur = self.head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        return length

    def get_kth_node_from_last(self, k):
        """
        연결 리스트의 마지막 노드부터 k 번째 노드의 데이터 구하기
        - k번째 노드 -> length - k
        :param k: (int) k번째 노드
        :return: k번째 노드
        """

        length = self.get_total_num_of_nodes()
        if 1 <= k <= length:
            kth_node_from_last = length - k
            cur = self.head
            cnt = 0
            while cur is not None:
                if cnt == kth_node_from_last:
                    return cur
                cur = cur.next
                cnt += 1


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(3).data)  # 7이 나와야 합니다!
