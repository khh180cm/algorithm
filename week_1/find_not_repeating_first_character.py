# 문자열에서 중복되지 않는 첫 알파벳 찾기
string = "akbacabade"


# 방법 1
def find_not_repeating_character_1(string):
    alpha_dict = {}
    for alpha in string:
        if alpha in alpha_dict:
            alpha_dict[alpha] += 1
        else:
            alpha_dict[alpha] = 1
    for key, value in alpha_dict.items():
        if value == 1:
            for i in string:
                if i == key:
                    return key
    return "_"


result = find_not_repeating_character_1(string)
print(result)


# 방법 2
def find_not_repeating_character_2(string):
    alpha_occur_list = [0] * 26
    for alpha in string:
        if alpha.isalpha():
            idx = ord(alpha) - ord('a')
            alpha_occur_list[idx] += 1
    not_repeating_char_list = []
    for idx in range(len(alpha_occur_list)):
        occur_cnt = alpha_occur_list[idx]
        if occur_cnt == 1:
            alpha = chr(idx + ord("a"))
            not_repeating_char_list.append(alpha)
    for i in string:
        if i in not_repeating_char_list:
            return i
    return "_"


result = find_not_repeating_character_2(string)
print(result)
