"""
키를 기준으로 정렬하기
"""

# 이름 오름차순
L1 = [
        {"name": "John", "score": 80},
        {"name": "Park", "score": 88},
        {"name": "Lee", "score": 28},
        {"name": "Hazard", "score": 78},
        {"name": "Zidane", "score": 8},
        {"name": "Brian", "score": 77},
]
res = sorted(L1, key=lambda x: x["name"])
print(res)

# 이름 내림차순
L2 = [
        {"name": "John", "score": 80},
        {"name": "Park", "score": 88},
        {"name": "Lee", "score": 28},
        {"name": "Hazard", "score": 78},
        {"name": "Zidane", "score": 8},
        {"name": "Brian", "score": 77},
]
res = sorted(L2, key=lambda x: x["name"], reverse=True)
print(res)


# 점수 오름차순
L3 = [
        {"name": "John", "score": 80},
        {"name": "Park", "score": 88},
        {"name": "Lee", "score": 28},
        {"name": "Hazard", "score": 78},
        {"name": "Zidane", "score": 8},
        {"name": "Brian", "score": 77},
]
res = sorted(L3, key=lambda x: x["score"])
print(res)


# 점수 내림차순
L4 = [
        {"name": "John", "score": 80},
        {"name": "Park", "score": 88},
        {"name": "Lee", "score": 28},
        {"name": "Hazard", "score": 78},
        {"name": "Zidane", "score": 8},
        {"name": "Brian", "score": 77},
]
res = sorted(L4, key=lambda x: x["score"], reverse=True)
print(res)
