"""
1부터 N까지 모든 자연수의 합을 구하시오
S(N) = N + S(N-1)
"""


def get_sum(num):
    if num == 1:
        return 1
    else:
        return num + get_sum(num-1)


res = get_sum(10)
print(res)
