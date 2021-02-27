"""
음이 아닌 정수들로 이뤄진 리스트
 - target 넘버를 만들기 위한 방법 리턴하기
"""


numbers = [1, 1, 1, 1, 1]
length = len(numbers)
target_number = 3
total_sum = []
total_count = 0
global cur_sum


def get_count_of_ways_to_target_by_doing_plus_or_minus(cur_idx, cur_sum, target):
    # 기저조건
    if cur_idx == length:
        if target == cur_sum:
            global total_count
            total_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(cur_idx + 1, cur_sum - numbers[cur_idx], target)
    get_count_of_ways_to_target_by_doing_plus_or_minus(cur_idx + 1, cur_sum + numbers[cur_idx], target)


get_count_of_ways_to_target_by_doing_plus_or_minus(0, 0, target_number)
print(total_count)
