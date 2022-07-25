"""
sorted로 리스트 정렬하기
"""
L = [3, 6, 2, -1, 50, 13, 37, 8]

# 1) 오름차순 정렬
ordered_L = sorted(L)
print(ordered_L)

# 2) 내림차순 정렬
ordered_L = sorted(L, reverse=True)
print(ordered_L)

"""
문자와 수로 구성된 리스트 정렬은 가능한가?
"""
# TypeError 발생
L = ["Baking", "123", 55]
try:
    print(L.sort())
except TypeError as e:
    print(f"{e}")
# 자체 로직으로 처리
res = sorted(
    L, key=lambda x: x if isinstance(x, int) else (ord(x[0]) if x.isalpha() else int(x))
)
print(res)

"""
문자열로 구성된 리스트가 있다.
- 문자열 길이 순 정렬
"""

L = [
    "BigO",
    "Array",
    "Hash Table",
    "Stack",
    "Queue",
    "Tree",
    "Graph",
    "SORTING",
    "BFS",
    "DFS",
    "Dynamic Programming",
    "dijkstra",
]
res = sorted(L, key=lambda x: len(x))
print(res)


"""
dict로 구성된 리스트가 있다.
"""
L = [
    {"name": "Coffee", "score": 87},
    {"name": "Greek Yogurt", "score": 70},
    {"name": "Meat", "score": 92},
]
res = sorted(L, key=lambda x: x["score"])
print(res)
