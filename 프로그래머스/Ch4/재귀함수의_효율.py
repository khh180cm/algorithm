"""
피보나치 수열로
반복 vs 재귀 효율 비교하기
"""


import time


def iter_fibo(N: int) -> int:
    """
    N번째 항의 피보나치 수 구하기
    """
    pass


def recur_fibo(N: int) -> int:
    pass


N = 20


t0 = time.time()
res = iter_fibo(N)
elapsed = time.time() - t0
print(f"Elapsed time: {elapsed:.2f}, 결과: {res}")

t0 = time.time()
res = recur_fibo(N)
elapsed = time.time() - t0
print(f"Elapsed time: {elapsed:.2f}, 결과: {res}")
