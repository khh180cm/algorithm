"""
소괄호 매칭 판별
"""

s = "(())()"


# 방법 1
def is_correct_parenthesis_1(string):
    try:
        # 개괄호 전용 스택
        stack = []
        for i in string:
            if i == "(":
                stack.append(i)
            else:
                # 폐괄호 있으면 개괄호 pop
                stack.pop()
        return True if not stack else False
    # 폐괄호 > 개괄호
    except IndexError:
        return False


print(is_correct_parenthesis_1(s))


# 방법 2
# def is_correct_parenthesis_2(string):
#    # 홀수 -> False
#    length = len(string)
#    if length % 2 == 1:
#        return False
#
#    open_bracket = 0
#    closed_bracket = 0
#    flag = True
#    for i in string:
#        if i == "(":
#            open_bracket += 1
#        else:
#            closed_bracket += 1
#        if closed_bracket > open_bracket:
#            flag = False
#            break
#    return flag
#
#
# print(is_correct_parenthesis_2(s))
