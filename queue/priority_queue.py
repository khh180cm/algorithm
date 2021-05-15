"""
Priority 큐
"""
import queue


# 우선순위 큐 정의 및 생성
data_queue = queue.PriorityQueue()

# 인큐
data_queue.put((7, "Korea"))
data_queue.put((9, "Turkey"))
data_queue.put((101, 1234))

# 큐 사이즈 확인
q_size = data_queue.qsize()
print(q_size)

# 디큐
res = data_queue.get()
print(res)
