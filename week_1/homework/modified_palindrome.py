# 펠린드롬 변형문제
import unittest


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    """
    :param string: 0과 1을 포함하는 문자열
    :return: 모든 1 또는 모든 0이 되기 위한 최소 변환 횟수
    """

    count_to_zeros = 0
    count_to_ones = 0

    if string[0] == '0':
        count_to_ones += 1
    else:
        count_to_zeros += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_ones += 1
            else:
                count_to_zeros += 1

    return min(count_to_ones, count_to_zeros)


if __name__ == "__main__":
    tester = unittest.TestCase()
    f_input = open("input_value.txt", "r")
    f_output = open("output_value.txt", "r")

    # input_value.txt
    input_number = f_input.read().splitlines()
    # output_value.txt
    output_number = f_output.read().splitlines()
    if input_number:
        for idx, each in enumerate(input_number):
            res = find_count_to_turn_out_to_all_zero_or_all_one(each)
            answer = int(output_number[idx])
            # 유닛 테스트
            tester.assertEqual(res, answer)
        print("Passed!")
    else:
        print("Parameter is not defined!")
    f_input.close()
    f_output.close()
