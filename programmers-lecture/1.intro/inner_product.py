"""
문제 설명
길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)
"""


def solution(a, b):
    res = is_validated(a, b)
    if not res:
        return False
    res = sum([a[i]*b[i] for i in range(len(a))])
    return res


def is_validated(a, b):
    flag = False
    if 1 <= len(a) <= 1000 and 1 <= len(b) <= 1000 and len(a) == len(b):
        for i in range(len(a)):
            if not (-1000 <= a[i] <= 1000 and -1000 <= b[i] <= 1000):
                flag = False
                break
        else:
            flag = True
    if flag:
        return True
    else:
        return False


a = [1, 2, 3, 4, -1]
b = [-3, -1, 0, 2, -1]
res = solution(a, b)
print(res)
