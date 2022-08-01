"""
피보나치 수열
- 반복 vs 재귀 효율 """


import time


def iter_fibo(N: int) -> int:
    """
    N번째 항의 피보나치 수 구하기
    """
    fibos = [1, 1]
    for _ in range(N):
        if len(fibos) < N:
            fibos.append(fibos[-1] + fibos[-2])
    return fibos[-1]


def recur_fibo(N: int) -> int:
    if N <= 2:
        return 1
    return recur_fibo(N - 1) + recur_fibo(N - 2)


N = 30


t0 = time.time()
res = iter_fibo(N)
elapsed = time.time() - t0
print(f"Elapsed time: {elapsed:.2f}, 결과: {res}")

t0 = time.time()
res = recur_fibo(N)
elapsed = time.time() - t0
print(f"Elapsed time: {elapsed:.2f}, 결과: {res}")
