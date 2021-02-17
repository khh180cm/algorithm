# 최빈값 찾기
sentence = "hello this is sparta"


# 방법 1
def find_max_occurred_alphabet(string):
    alphabet_occurrence = [0] * 26
    std_asci = ord("a")
    # 알파벳 빈도수 카운트
    for each in string:
        if each.isalpha():
            asci_num = ord(each)
            idx = asci_num - std_asci
            alphabet_occurrence[idx] += 1

    # 최빈값 찾기
    for idx, num in enumerate(alphabet_occurrence):
        max_num = alphabet_occurrence[0]
        if num > max_num:
            max_idx = idx
    alpha = chr(std_asci + max_idx)
    return alpha


result = find_max_occurred_alphabet(sentence)
print(result)


# 방법 2
def find_max_occurred_alphabet_2(string):
    # 공백 제거
    string = sentence.replace(" ", "")
    alphabet_occurrence = [0] * 26
    std_asci = ord("a")
    # 알파벳 빈도수 카운트
    for each in string:
        if each.isalpha():
            asci_num = ord(each)
            idx = asci_num % std_asci
            alphabet_occurrence[idx] += 1

    # 최빈값 찾기
    for idx, num in enumerate(alphabet_occurrence):
        max_num = alphabet_occurrence[0]
        if num > max_num:
            max_idx = idx
    alpha = chr(std_asci + max_idx)
    return alpha


result = find_max_occurred_alphabet_2(sentence)
print(result)
