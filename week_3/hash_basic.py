"""
딕셔너리 내부 구조는 배열로 구성
"""

# 데이터 저장 -> O(1)
items = [None] * 8
items[hash("slow") % 8] = "느린"
items[hash("fast") % 8] = "빠른"

print(items)

# 데이터 검색 -> O(1)
res = items[hash("slow") % 8]
print(res)
