"""
리스트의 마지막이 아닌 곳에 원소를 추가하거나 제거하기
- 상수 시간: O(N)
"""

# 원소 추가
num_list = [20, 10, 33, 175, 177, 190]

num_list.insert(3, 1111)
print(num_list)

# 원소 제거
del num_list[2]
print(num_list)
