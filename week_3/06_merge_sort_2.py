"""
merge sort
- 단어 vocabulary 정렬하기
"""
arr = ["y", "r", "a", "l", "u", "b", "a", "c", "o", "v"]


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])
    return merge(left_arr, right_arr)


def merge(arr1, arr2):
    arr1_left = 0
    arr2_left = 0
    arr1_length = len(arr1)
    arr2_length = len(arr2)
    new_list = []
    while arr1_left < arr1_length and arr2_left < arr2_length:
        if arr1[arr1_left] < arr2[arr2_left]:
            new_list.append(arr1[arr1_left])
            arr1_left += 1
        else:
            new_list.append(arr2[arr2_left])
            arr2_left += 1
    if arr1_left == len(arr1):
        return new_list + arr2[arr2_left:]
    else:
        return new_list + arr1[arr1_left:]


res = merge_sort(arr)
print(res)
