"""
팩토리얼
"""


def get_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * get_factorial(n-1)


res = get_factorial(5)
print(res)
