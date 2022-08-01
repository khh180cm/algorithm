"""
서로 다른 N개의 원소 중 m개를 택하는 경우의 수
"""
from math import factorial as f

# 1


def get_factorial_by(N: int) -> int:
    if N <= 1:
        return N
    return N * get_factorial_by(N - 1)


def get_nCr(n: int, r: int) -> int:
    return get_factorial_by(n) // (get_factorial_by(n - r) * get_factorial_by(r))


res = get_nCr(5, 2)
print(res)

# 2


def combi(m: int, n: int) -> int:
    if m == n:
        return 1
    elif m <= 0:
        return 1
    else:
        return combi(m - 1, n) + combi(m - 1, n - 1)


res = combi(5, 3)
print(res)
