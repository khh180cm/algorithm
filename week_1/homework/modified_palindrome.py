import unittest
# 펠린드롬 변형문제


def find_count_to_turn_out_to_all_zero_or_all_one(string):
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

    input_number = f_input.read().splitlines()
    output_number = f_output.read().splitlines()
    if input_number:
        for idx, each in enumerate(input_number):
            res = find_count_to_turn_out_to_all_zero_or_all_one(each)
            answer = int(output_number[idx])
            tester.assertEqual(res, answer)
        print("Passed!")
    else:
        print("Parameter is not defined!")
    f_input.close()
    f_output.close()
