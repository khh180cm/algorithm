"""
피보나치 수열
- 재귀함수 사용
"""

input_num = 70


def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input_num))
