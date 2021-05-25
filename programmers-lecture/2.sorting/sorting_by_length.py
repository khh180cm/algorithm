"""
문자열 길이를 기준으로 정렬
"""

# 1. 문자열로 구성된 리스트 정렬시, 알파벳 순임
str_arr = ['c', 'o', 'm', 'p', 'u', 't', 'e', 'r']
str_arr.sort()
print(str_arr)

# 2. 문자열의 길이를 기준으로 정렬
# 1)
L1 = ["abcde", "def", "ghijklmnop", "qrs"]
res = sorted(L1, key=lambda x: len(x))
print(res)

# 2)
L2 = ["abcde", "def", "ghijklmnop", "qrs"]
L2.sort(key=len)
print(L2)
