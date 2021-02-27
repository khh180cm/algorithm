"""
회문(palindrome)
 - 1) 재귀 함수 방식
 - 2) 반복문 while 방식
 - 3) 반복문 for 방식

Ex) "가련하시다 사장 집 아들 딸들아 집 장사 다시 하련가"
"""

sentence = "가련하시다 사장 집 아들 딸들아 집 장사 다시 하련가"
sentence = sentence.replace(" ", "")
# sentence = "안녕녕안"


# 1-1) 재귀 함수 활용
def is_palindrome_by_recursion_1(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 2:
        return True
    return is_palindrome_by_recursion_1(string[1:-1])


res = is_palindrome_by_recursion_1(sentence)
print(res)


# 1-2) 재귀 함수 활용
def is_palindrome_by_recursion_2(string):
    left = 0
    right = len(string)
    if left == right:
        return True
    if string[left] != string[right - 1]:
        return False

    return is_palindrome_by_recursion_2(string[left + 1:right - 1])


res = is_palindrome_by_recursion_2(sentence)
print(res)


# 1-3) 재귀 함수 활용
def is_palindrome_by_recursion_3(string):
    n = len(string)
    i = 0
    if not string:
        return True
    i += 1
    string = string[i:n-i]
    return is_palindrome_by_recursion_3(string)


res = is_palindrome_by_recursion_2(sentence)
print(res)


# 2. 반복문(while) 활용
def is_palindrome_by_while(string):
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


res = is_palindrome_by_while(sentence)
print(res)


# 3. 반복문(for) 활용
def is_palindrome_by_for(string):
    length = len(string)
    for i in range(length):
        if not string[i] == string[length - 1 - i]:
            return False
    return True


res = is_palindrome_by_for(sentence)
print(res)
