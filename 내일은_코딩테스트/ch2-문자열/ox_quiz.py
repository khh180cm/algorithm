"""
[문제]
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z'형태로 들어 있는 문자열 배열 quiz가
매개변수로 주어진다.
수식이 옳다면 'O'를, 틀리다면 'X'를 순서대로 담은 배열을 리턴하는 solution 함수를 완성해라.

[제한 사항]
연산 기호와 숫자 사이는 항상 하나의 공백이 존재한다.
단, 음수를 표시하는 마이너스 기호와 숫자 사이에는 공백이 존재하지 않는다.
1 <= quiz의 길이 <= 10
X, Y, Z는 각각 0부터 9까지 이뤄진 정수를 의미하며,
각 숫자의 맨 앞에 마이너스 기호가 있을 수 있으며 이는 음의 정수를 의미한다.
+, - 연산자만 존재

[입출력 예시]
quiz                                                       result
["3 - 4 = -3", "5 + 6 = 11"]                               ["X", "O"]
["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"] ["O", "O", "X", "O"]

"""

quiz_list = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]

def solution1(quiz_list):
    ans = []
    for quiz in quiz_list:
        quiz_not_resolved, expected = quiz.split("=")
        if sum(int(i) for i in quiz_not_resolved.replace("- ", "+ -").split("+")) == int(expected):
            ans.append("O")
        else:
            ans.append("X")
    return ans

print(solution1(quiz_list))


def solution2(quiz_list):
    ans = []
    for quiz in quiz_list:
        res = 0
        left, right = quiz.split("=")
        num1, operator, num2 = left.split()
        if operator == "+":
            left = int(num1) + int(num2)
        else:
            left = int(num1) - int(num2)

        ans.append("O" if left == int(right) else "X")
    return ans


print(solution2(quiz_list))