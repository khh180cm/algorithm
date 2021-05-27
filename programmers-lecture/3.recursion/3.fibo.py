"""
피보나치 순열
S(n) = S(n-1) + S(n-2), n>=2
"""


def fibo_with_recursive(n):
    if n <= 2:
        return 1
    else:
        return fibo_with_recursive(n-1) + fibo_with_recursive(n-2)


res = fibo_with_recursive(6)
print(res)
