"""
LIFO 큐
"""

import queue


# 인큐
data_queue = queue.LifoQueue()
data_queue.put("fun coding")
data_queue.put(1)


# 큐 사이즈 확인
q_size = data_queue.qsize()
print(q_size)

# 디큐
res = data_queue.get()
print(res)
