"""
순차 탐색
"""

finding_number = 14
seq_list = [i for i in range(1, 15)]


def is_exist(target, array):
    for i in array:
        if i == target:
            return True
    return False


res = is_exist(finding_number, seq_list)
print(res)
