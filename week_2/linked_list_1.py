"""
간단한 Linked List
- 노드 개별 지정하는 방식
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 티파니 노드
a = Node("티파니")
# 서현 노드
b = Node("서현")
# 태연 노드
c = Node("태연")

# 노드 연결하기
# a -> b -> c
a.next = b
b.next = c
