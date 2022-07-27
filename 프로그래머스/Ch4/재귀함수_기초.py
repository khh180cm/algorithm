"""
1부터 N까지의 합을 재귀함수로 구하기
"""
N = 100


def get_sum_recursively(N: int) -> int:
    if N <= 1:
        return N
    else:
        return N + get_sum_recursively(N - 1)


res = get_sum_recursively(N)
print(res)


"""
cf) 재귀 함수보다 더 효율적인 방식이 있는지 항상 고민해야 한다.
- O(1)
"""


def get_sum_efficiently(N: int) -> int:
    return N(N + 1) // 2


res = get_sum_recursively(N)
print(res)
