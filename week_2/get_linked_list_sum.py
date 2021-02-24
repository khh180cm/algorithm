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


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 방법 1
    sum_1 = _get_linked_list_sum(linked_list_1)
    sum_2 = _get_linked_list_sum(linked_list_2)

    return sum_1 + sum_2

    # 방법 2
    # first_lnk_list = []
    # second_lnk_list = []
    # # 리스트에 노드 값 넣기
    # while linked_list_1.head:
    #     first_lnk_list.append(linked_list_1.head.data)
    #     linked_list_1.head = linked_list_1.head.next
    # while linked_list_2.head:
    #     second_lnk_list.append(linked_list_2.head.data)
    #     linked_list_2.head = linked_list_2.head.next

    # # 총합 구하기
    # first_sum = 0
    # first_lnk_list = sorted(first_lnk_list, reverse=True)
    # for i in range(len(first_lnk_list)):
    #     first_sum += first_lnk_list[i] * (10 ** i)
    # second_sum = 0
    # second_lnk_list = sorted(second_lnk_list, reverse=True)
    # for i in range(len(second_lnk_list)):
    #     second_sum += second_lnk_list[i] * (10 ** i)
    # return first_sum + second_sum


def _get_linked_list_sum(linked_list):
    """
    각 노드 값의 합을 구하되, 자릿수 고려
    Ex) [6] -> [7] -> [8] == 678
    """

    total = 0
    head = linked_list.head
    while head:
        total = total * 10 + head.data
        head = head.next
    return total


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
