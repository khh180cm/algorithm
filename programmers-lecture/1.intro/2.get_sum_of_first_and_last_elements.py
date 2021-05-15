"""
입력으로 주어지는 리스트의 첫 원소와 마지막 원소의 합을 리턴
"""


def solution(x):
    assert isinstance(x, list) and x and all(isinstance(i, int) for i in x), 'Value error!!!'

    first_element = x[0]
    last_element = x[-1]
    return first_element + last_element


res = solution([i for i in range(11)])
print(f'해는 {res}')
