input_num = 2


def find_prime_list_under_number(number):
    """
    number 미만의 소수들을 구하는 헬퍼 함수
    ex) 7 -> [2, 3, 5]

    :param number: 양의 정수
    :return: 소수들로 이루어진 리스트
    """

    prime_list = []
    for divisor in range(2, number):
        for divided_by in range(2, divisor):
            # 나머지가 0일 때 -> 소수 조건 미충족
            if divisor % divided_by == 0:
                break
        else:
            prime_list.append(divisor)
    return prime_list


result = find_prime_list_under_number(input_num)
print(result)
