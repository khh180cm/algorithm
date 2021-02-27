"""
재귀를 활용한 팩토리얼
"""


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


print(factorial(5))

