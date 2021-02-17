# 숫자로 이루어진 배열의 최댓값을 구하기
num_list = [3, 5, 6, 1, 2, 4]

# 방법 1
max_num = num_list[0]
for num in num_list:
    if num > max_num:
        max_num = num
print(f"최댓값은 {max_num}")


# 방법 2
max_num = float("-inf")
for num in num_list:
    if num > max_num:
        max_num = num
print(f"최댓값은 {max_num}")


# 방법 3
length = len(num_list)
for i in range(length):
    tmp_max = num_list[i]
    is_find = False
    for j in range(length):
        if num_list[j] > tmp_max:
            break
        elif j == length -1:
            is_find = True
            break
    if is_find:
        break
print(f"최댓값은 {tmp_max}")


# 방법 4
max_num = float("-inf")
for num in num_list:
    for compare_num in num_list:
        if compare_num > num:
            break
    else:
        max_num = num
        break
print(f"최댓값은 {max_num}")


# 방법 5 - 부분 버블정렬
length = len(num_list)
i = 0
while (i + 1) < length:
    if num_list[i] > num_list[i+1]:
        num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
    i += 1
max_num = num_list[length-1]
print(f"최댓값은 {max_num}")


# 방법 6
num_list.sort(reverse=True)
max_num = num_list[0]
print(f"최댓값은 {max_num}")