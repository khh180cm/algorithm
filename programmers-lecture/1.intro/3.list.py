# 리스트 길이와 무관 O(1)

L = ["Bob", "Cat", "Spam", "Programmers"]
print(L[1])
print(L[-2])

L.append("New")
res = L.pop()

# 원소 추가 O(N)
target = 65
L = [20, 37, 58, 72, 91]
for i in range(len(L)):
    if L[i] >= 65:
        L.insert(i, target)
        break
print(L)

# 원소 삭제 O(N)
target = 58
for i in range(len(L)):
    if L[i] == target:
        L.pop(i)
        break
print(L)
