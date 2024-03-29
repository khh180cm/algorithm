"""
상수 복잡도 O(1)
- 입력 데이터 크기와 관계없이 항상 같은 단계의 연산이 수행되는 알고리즘의 성능 평가
"""


def constant_time_algorithm(items):
    """데이터 크기와 관계없이 5번째 인덱스의 데이터만 매번 가져온다"""

    result = items[5] * items[5]
    print(result)


constant_time_algorithm(list(range(100)))


"""
데이터 크기가 10개, 1000개, 10000000개에 관계없이 항상 5번째 인덱스의 값을 읽고 제곱한다
그리곤 print함수를 작동시킨다.
엄밀히는 O(1+1)이나, 항상 같은 연산량임을 나타내기 위해 O(1)이라 표현한다.

즉, 데이터 크기에 관계없이 1000번의 연산이 수행된다면, 이때 역시 O(1)이 된다.
알고리즘의 성능 평가는 데이터 크기 대비 수행되는 연산의 수로 측정되기 때문이다.
"""
