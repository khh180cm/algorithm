"""
[문제]
my_string과 정수 num1, num2가 매개변수로 주어진다
my_string에서 인덱스 num1과 인덱스 num2에 해당하는
문자열을 리턴하는 solution 함수를 완성해라.

[제한 사항]
1 <= my_string의 길이 <= 100
0 <= num1, num2 <= my_string의 길이
my_string은 소문자로 이뤄져 있다
num1 != num2

[입출력 예시]
my_string    num1 num2 result
"hello"      1    2    "hlelo"
"I love you" 3    6    "I l voyou"
"""

my_string = "I love you"


# 방법 1
def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return "".join(my_string)


print(solution(my_string, 3, 6))


# 방법 2
def solution(my_string, num1, num2):
    small, big = sorted((num1, num2))
    return (
        my_string[:small]
        + my_string[big]
        + my_string[small + 1 : big]
        + my_string[small]
        + my_string[big + 1 :]
    )


print(solution(my_string, 3, 6))
