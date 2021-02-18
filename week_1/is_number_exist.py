# 리스트에 특정 숫자 존재 여부 체크
num_arr = [3, 5, 6, 1, 2, 4]


# 방법 1
def is_number_exist_1(number, num_arr):
    # 반복문 내 비교 연산
    for each in num_arr:
        if number == each:
            return True
    return False


result = is_number_exist_1(2, num_arr)
print(result)


# 방법 2
def is_number_exist_2(number, num_arr):
    # 리스트 메소드 및 raise Error 활용
    try:
        num_arr.remove(number)
        return True
    except ValueError:
        return False


result = is_number_exist_2(3, num_arr)
print(result)


# 방법 3
def is_number_exist_3(number, array):
    return True if number in array else False


num_arr = [3, 5, 6, 1, 2, 4]
result = is_number_exist_3(3, num_arr)
print(result)
