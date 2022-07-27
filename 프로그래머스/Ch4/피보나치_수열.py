"""
재귀함수를 활용한 피보나치 수열
Q. N 이하의 피보나치 수열을 구현하기
*피보나치 수열: 첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열
"""
from typing import List

N = 10


def get_fibos_below(N: int, res: List) -> List:
    n2 = res[-2] + res[-1]
    if n2 > N:
        return res
    else:
        res.append(n2)
        return get_fibos_below(N, res)


res = get_fibos_below(N, [1, 1])
print(res)


"""
인자로 0 또는 양의 정수인 x 가 주어질 때,
피보나치 수열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.
"""


def get_fibo_of(N: int) -> int:
    if N <= 1:
        return 1
    return get_fibo_of(N - 1) + get_fibo_of(N - 2)


res = get_fibo_of(N)
print(res)
