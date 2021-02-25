"""
이진 탐색
"""

finding_number = 14
seq_list = [i for i in range(1, 15)]


def is_exist(target, array):
    # 방법 1
    cur_min_idx = 0
    cur_max_idx = len(array) - 1
    cur_guess_idx = (cur_min_idx + cur_max_idx) // 2
    while cur_min_idx <= cur_max_idx:
        if array[cur_guess_idx] == target:
            return True
        elif array[cur_guess_idx] > target:
            cur_max_idx = cur_guess_idx - 1
        else:
            cur_min_idx = cur_guess_idx + 1
        cur_guess_idx = (cur_min_idx + cur_max_idx) // 2
    return False

    # # 방법 2
    # middle_idx = len(array) // 2
    # while array:
    #     middle_value = array[middle_idx]
    #     if target > middle_value:
    #         array = array[middle_idx+1:]
    #     elif target < middle_value:
    #         array = array[:middle_idx]
    #     else:
    #         return True
    #     middle_idx = len(array) // 2
    # return False


res = is_exist(14, seq_list)
print(res)
