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
    # 알파벳 빈도 카운트
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


# 방법 3
def find_max_occurred_alphabet_3(string):
    string = string.replace(" ", "")
    alphabet = [chr(i) for i in range(97, 123)]
    alphabet_occurrence = [0] * 26

    for each in alphabet:
        # 이중 for문으로 빈도 카운트
        for compare_each in string:
            if each == compare_each:
                asci_num = ord(each)
                idx = asci_num - ord("a")
                alphabet_occurrence[idx] += 1

    # 최댓값 찾기
    max_num = float("-inf")
    max_idx = 0
    for idx, cnt in enumerate(alphabet_occurrence):
        if cnt > max_num:
            max_num = cnt
            max_idx = idx
    return alphabet[max_idx]


result = find_max_occurred_alphabet_3(sentence)
print(result)


# 방법 4
def find_max_occurred_alphabet_4(string):
    string = string.replace(" ", "")
    alphabet = [chr(i) for i in range(97, 123)]

    max_occurrence = 0
    max_alphabet = alphabet[0]
    for each in alphabet:
        occurrence = 0
        for compare_each in string:
            if each == compare_each:
                occurrence += 1
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = each
    return max_alphabet


result = find_max_occurred_alphabet_4(sentence)
print(result)