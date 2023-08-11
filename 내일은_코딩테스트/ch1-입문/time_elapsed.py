"""
임의의 숫자가 데이터에 존재하는지 확인하는 알고리즘
"""


import time

N = 100000
FIND = 50000


def find_value_in_data(find, nums):
    return find in nums


nums_list = list(range(N))
nums_dict = {i: i for i in range(N)}


start = time.time()
find_value_in_data(FIND, nums_list)
print(f"Elapsed: {time.time() - start : .5f} sec")


start = time.time()
find_value_in_data(FIND, nums_dict)
print(f"Elapsed: {time.time() - start : .5f} sec")

"""
리스트일 때와 딕셔너리일 때 코드가 실행되는 데 필요한 시간이 확실히 다르다.
하지만 이러한 방법을 표준으로 채택할 수 없다
시간을 측정하는 컴퓨터마다 소요되는 시간이 다르기 때문이다.
즉,
- "내 알고리즘이 반영된 소스 코드가 배포가 될 때, 어떤 서버를 기준으로 할까"
- "같은 서버라도 네트워크 상황마다 다르게 실행될 여지가 있다"
따라서, 우리는 알고리즘은 아래와 같이 평가한다.
"데이터 크기 대비 프로그램이 실행하는데 필요한 단계 수로 평가한다."
"""
