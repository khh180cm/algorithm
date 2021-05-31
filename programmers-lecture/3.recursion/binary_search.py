"""
리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어지고, 또한 탐색의 대상이 되는 리스트 내에서의 범위 인덱스가 l 부터 u 까지로 (인자로) 정해질 때, x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다. 리스트 L 은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다. 또한, 동일한 원소는 두 번 이상 나타나지 않습니다.

인덱스 범위를 나타내는 l 과 u 가 인자로 주어지는 이유는, 이 함수를 재귀적인 방법으로 구현하기 위함입니다. 빈 칸에 알맞은 내용을 채워서 재귀 함수인 solution() 을 완성하세요.

예를 들어,
L = [2, 3, 5, 6, 9, 11, 15]
x = 6
l = 0
u = 6
의 인자들이 주어지면, L[3] == 6 이므로 3 을 리턴해야 합니다.

또 다른 예로,
L = [2, 5, 7, 9, 11]
x = 4
l = 0
u = 4
로 주어지면, 리스트 L 내에 4 의 원소가 존재하지 않으므로 -1 을 리턴해야 합니다.
"""


def binary_search(L, left, right, target):
    if left > right:
        return -1
    else:
        middle = (left + right) // 2
        if L[middle] > target:
            return binary_search(L, left, middle-1, target)
        elif L[middle] < target:
            return binary_search(L, middle+1, right, target)
        else:
            return middle


int_arr = [2, 3, 5, 6, 9, 11, 15]
x = 10
l = 0
r = 6

res = binary_search(int_arr, l, r, x)
print(res)
