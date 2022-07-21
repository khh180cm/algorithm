"""
리스트의 마지막이 아닌 곳에 원소를 추가하거나 제거하기
- 선형 시간: O(N)
"""

# 원소 추가
num_list = [20, 10, 33, 175, 177, 190]

num_list.insert(3, 1111)
print(num_list)

# 원소 제거
del num_list[2]
print(num_list)

# 원소 탐색하기
try:
    res = num_list.index(2000000)
    print(res)
except ValueError as e:
    print(e)
