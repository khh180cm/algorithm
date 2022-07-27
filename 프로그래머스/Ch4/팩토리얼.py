"""
팩토리얼을 재귀 함수로 구현하기
"""
N = 5


def get_factorial_by(N: int) -> int:
    if N <= 1:
        return N
    return N * get_factorial_by(N - 1)


res = get_factorial_by(N)
print(res)
