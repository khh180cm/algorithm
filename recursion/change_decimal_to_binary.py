"""
재귀함수를 이용하여 십진수를 이진수로 바꿔 출력하기
"""


def change_to_binary(decimal):
    if decimal <= 1:
        return decimal
    else:
        quotient = decimal // 2
        remainder = decimal % 2
        return remainder + 10 * change_to_binary(quotient)


res = change_to_binary(10)
print(res)
