"""
정렬되지 않은 배열에 이진탐색 적용시 문제점
"""
finding_target = 2
unordered_numbers = [0, 3, 5, 6, 1, 2, 4]
ordered_numbers = sorted(unordered_numbers, reverse=False)


def is_exist_target_number_binary(target, numbers):
    left = 0
    right = len(numbers) - 1
    middle = (left + right) // 2
    while left <= right:
        if target == numbers[middle]:
            return True
        elif target < numbers[middle]:
            right = middle - 1
        else:
            left = middle + 1
        middle = (left + right) // 2
    return False


result_1 = is_exist_target_number_binary(finding_target, unordered_numbers)
print(result_1)

result_2 = is_exist_target_number_binary(finding_target, ordered_numbers)
print(result_2)
