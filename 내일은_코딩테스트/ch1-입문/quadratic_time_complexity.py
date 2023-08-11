"""
이차 복잡도 O(n^2)
- 입력 데이터 크기 N에 따라 수행 단계가 제곱이 되는 알고리즘 성능 평가
"""


def quadratic_algorithm(items):
    for i in items:
        for j in items:
            print(i, " ", j)


quadratic_algorithm([i for i in range(5)])
