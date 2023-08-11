"""
[문제]
문자열 my_string이 매겨변수로 주어진다.
my_string은 소문자, 대문자, 자연수로만 구성 돼 있다.
my_string 안의 자연수들의 합을 리턴하는 solution 함수를 완성해라.

[제한 사항]
0 <= my_string의 길이 <= 1000
1 <= my_string안의 자연수 <= 1000
연속된 수는 하나의 수로 간주한다
000123과 같이 0이 선행하는 경우는 없다
문자열에 자연수가 없는 경우 0을 리턴한다

[입출력 예시]
my_string       result
"aAb1B2cC34oOp" 37
"1a2b3c4d123Z"  133
"""


# 방법 1
my_string = "1a2b3c4d123Z"


def solution(my_string):
    ans = []
    last_char = ""
    for char in my_string:
        if char.isdigit():
            if last_char.isdigit():
                ans[-1] += char
            else:
                ans.append(char)
        last_char = char
    if ans:
        return sum(int(i) for i in ans)
    else:
        return 0


print(solution(my_string))


# 방법 2
def solution(my_string):
    ans = 0
    temp = ""
    for char in my_string:
        if char.isdigit():
            temp += char
        else:
            if temp:
                ans += int(temp)
                temp = ""
    return ans


print(solution(my_string))


# 방법 3
def solution(my_string):
    my_string = "".join([char if char.isdigit() else " " for char in my_string])
    return sum(int(char) for char in my_string.split())


print(solution(my_string))


# 방법 4
def solution(my_string):
    import re

    my_string = re.findall(r"[0-9]+", my_string)
    return sum(int(char) for char in my_string)


print(solution(my_string))
