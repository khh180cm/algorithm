"""
[문제]
머쓱이는 태어난 지 6개월 된 조카를 돌보고 있다.
조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩만 사용해 조합한(이어 붙인)
발음 밖에 하지 못한다. 문자열 배열 babbling이 매개변수로 주어질 때,
머쓱이의 조카가 발음할 수 있는 단어의 갯수를 리턴하도록 solution 함수를 완성해라.

[제한 사항]
1 <= babbling의 길이 <=100
1 <= babbling[i]의 길이 <= 15
babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장한다.
각 문자열은 모두 소문자로만 이뤄져 있다.

[입출력 예시]
["aya", "yee", "u", "maa", "wyeoo"] -> 1
["ayaye", "uuuma", "ye", "yemawoo", "ayaa"] -> 3
"""


def solution(given_list):
    words = ["aya", "ye", "woo", "ma"]
    talkable = set()
    talkable.add("".join(words))

    cnt = 0
    for i in words:
        for j in words:
            for k in words:
                if i == j == k:
                    talkable.add(i)
                elif (i == j) and (j != k):
                    talkable.add(i + k)
                elif (i != j) and (j != k) and (k != i):
                    talkable.add(i + j + k)
    for i in given_list:
        if i in talkable:
            cnt += 1
    return cnt


res = solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])
print(res)


def solution2(given_list):
    words = ["aya", "ye", "woo", "ma"]
    talkable = set()
    talkable.add("".join(words))

    cnt = 0
    for i in words:
        talkable.add(i)
        for j in words:
            if i == j:
                continue
            for k in words:
                talkable.add(i + j)
                if j == k:
                    continue
                talkable.add(i + j + k)
    for i in given_list:
        if i in talkable:
            cnt += 1
    return cnt


res = solution2(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])
print(res)


def solution3(given_list):
    cnt = 0
    words = ["aya", "ye", "woo", "ma"]
    for given in given_list:
        for word in words:
            given = given.replace(word, " ")
        if not given.strip():
            cnt += 1
    return cnt


res = solution3(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])
print(res)
