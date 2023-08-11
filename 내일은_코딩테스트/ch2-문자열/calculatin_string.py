"""
[문제]
my_string은 "3+5"처럼 문자열로 된 수식이다.
문자열 my_string이 매개변수로 주어질 때,
수식을 계산한 값을 리턴하는 solution 함수를 완성해라.

[제한 사항]
+, - 연산자만 존재
문자열의 시작과 끝에는 공백 없음
0으로 시작하는 숫자는 없음
잘못된 수식 없음
5 <= my_string의 길이 <= 100
결과값은 1이상 100,000이하
my_string의 숫자와 연산자는 공백 하나로 구분

[입출력 예시]
my_string result
"3 + 4"   7
"""


my_string = "3 - 4"


# 방법 1
def solution1(my_string):
    if "+" in my_string:
        first, second = my_string.split(" + ")
        return int(first) + int(second)
    else:
        first, second = my_string.split(" - ")
        return int(first) - int(second)


res = solution1(my_string)
print(res)


# 방법 2
def solution2(my_string):
    return sum(int(i) for i in my_string.replace("- ", "+-").split("+"))


res = solution2(my_string)
print(res)


# 방법 3
def solution3(my_string):
    my_string = my_string.split()
    operator = ""
    res = 0
    for char in my_string:
        if char in ["+", "-"]:
            operator = char
        else:
            if operator == "+":
                res += int(char)
            elif operator == "-":
                res -= int(char)
            else:
                res = int(char)
    return res


res = solution3(my_string)
print(res)
