"""
로그 복잡도 O(logn)
- 입력 데이터 크기 N에 따라 수행 단계가 logN으로 줄어드는 알고리즘 성능 평가
"""


find = -1
ordered_list = list(range(10))


def find_value(find, data):
    mid_idx = len(data) // 2

    # 방법 1
    try:
        if data[mid_idx] > find:
            return find_value(find, data[:mid_idx])
        elif data[mid_idx] < find:
            return find_value(find, data[mid_idx + 1 :])
        else:
            return True
    except IndexError:
        return False

    # 방법 2
    while data:
        if data[mid_idx] > find:
            return find_value(find, data[:mid_idx])
        elif data[mid_idx] < find:
            return find_value(find, data[mid_idx + 1 :])
        else:
            return True
    return False


print(find_value(find, ordered_list))
