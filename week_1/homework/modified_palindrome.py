# 펠린드롬 변형문제
# input_num = "00010000001"
input_num = "0100"
# input_num = "1011"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    """
    :param string: 0 또는 1로 이뤄진 문자열
    :return: 0을 포함한 양의 정수
            전부 1 또는 전부 0으로 만들기 위한 최소 변환 횟수
    """

    count_to_ones = 0
    count_to_zeros = 0
    for idx in range(len(string)-1):
        if string[idx] == "0":
            if string[idx] != string[idx+1]:
                count_to_ones += 1
            else:
                if len(string) - 1 == idx + 1:
                    count_to_ones += 1
                else:
                    count_to_zeros += 1
        else:
            if string[idx] != string[idx+1]:
                count_to_zeros += 1
            else:
                if len(string) - 1 == idx + 1:
                    count_to_zeros += 1
                else:
                    count_to_ones += 1
    return min(count_to_zeros, count_to_ones)


res = find_count_to_turn_out_to_all_zero_or_all_one(input_num)
print(res)
