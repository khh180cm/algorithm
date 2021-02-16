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


# 방법 3 - 부분 버블정렬
length = len(num_list)
idx = 0
while idx + 1 < length:
    if num_list[idx] > num_list[idx+1]:
        num_list[idx], num_list[idx+1] = num_list[idx+1], num_list[idx]
    idx += 1
max_num = num_list[length-1]
print(f"최댓값은 {max_num}")


# 방법 4
num_list.sort(reverse=True)
max_num = num_list[0]
print(f"최댓값은 {max_num}")