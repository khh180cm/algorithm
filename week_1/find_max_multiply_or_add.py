"""
### 페이스북 알고리즘 문제 ###

0과 자연수로 이루어진 리스트에
+ 혹은 X 를 활용하여 최댓값 구하기
단, 앞에서부터 연산이 진행된다.

Ex) 아래의 결과는  728
0 + 3 * 5 * 6 + 1 * 2 * 4

"""

num_arr = [0, 3, 5, 6, 1, 2, 4]


# 방법 1
def find_max_plus_or_multiply_1(num_arr):
    cur_sum = 0
    for i in range(len(num_arr)):
        if i == len(num_arr) - 1:
            max_num = cur_sum
            return max_num
        plus_result = cur_sum + num_arr[i + 1]
        multiply_result = cur_sum * num_arr[i + 1]
        if plus_result > multiply_result:
            cur_sum = plus_result
        else:
            cur_sum = multiply_result


result = find_max_plus_or_multiply_1(num_arr)
print(result)


# 방법 2
def find_max_plus_or_multiply_2(num_arr):
    cur_sum = 0
    for num in num_arr:
        if num <= 1 or cur_sum <= 1:
            cur_sum += num
        else:
            cur_sum *= num
    return cur_sum


result = find_max_plus_or_multiply_2(num_arr)
print(result)
