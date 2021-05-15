"""
큐 구현해보기
- 리스트 기반
"""


class QueueList:
    def __init__(self):
        self.queue_list = []

    def enqueue(self, data):
        self.queue_list.append(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        return self.queue_list.pop(0)

    def is_empty(self):
        return False if self.queue_list else True

    def q_size(self):
        return len(self.queue_list)


# 큐 정의 및 생성
queue_list = QueueList()

# 인큐
queue_list.enqueue(1)
queue_list.enqueue(9)
queue_list.enqueue(10)

# 큐 사이즈
q_size = queue_list.q_size()
print(q_size)

# 디큐
while True:
    try:
        res = queue_list.dequeue()
        print(res)
    except IndexError:
        break

