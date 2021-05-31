"""
피보나치 순열
S(n) = S(n-1) + S(n-2), n>=2
"""


# 1. 재귀
def fibo_with_recursive(n):
    if n <= 1:
        return n
    else:
        return fibo_with_recursive(n-1) + fibo_with_recursive(n-2)


res1 = fibo_with_recursive(6)
print(res1)


# 2. 반복
def fibo_with_iterative(n):
    memory = {
        0: 0,
        1: 1,
    }
    for i in range(n):
        if i not in memory.keys():
            memory[i] = memory[i-1] + memory[i-2]
    return memory[n-1] + memory[n-2]


res2 = fibo_with_iterative(6)
print(res2)
