"""
[자료구조와 알고리즘은 왜 중요한가]

1. 자료구조에 대한 의문들
- 1) 리스트, 딕셔너리, 튜플, 세트 등의 기본 자료구조를 제공하고 있다.
- 2) 그럼에도 우리는 왜 자료구조를 따로 배워야하는 것일까?

2. 알고리즘에 대한 의문들
- 자료구조도 복잡한데, 알고리즘은 또 무엇인가
- ex) 아래 두 상황에서 느끼는 감정은?
    - 아무런 규칙없이 나열된 100,000개의 수들 중에서 549를 찾기
    - 오름차순으로 정렬된 100,000개의 수들 중에서 549를 찾기
- 왜 어떤 건 솔루션을 찾기가 어렵다고 느끼고, 어떤 건 쉽다고 느껴지는 걸까?

3. 자료구조와 알고리즘의 중요성
- 주어진 문제를 효율적으로 해결하는 방법에 대한 고민
    -> 적절한 자료구조와 연산 방법에 대한 선택
- 해결하고자 하는 문제에 따라 최적의 자료구조/알고리즘을 선택할 수 있어야 함
- 이 선택을 제대로 하기 위해 자료구조와 알고리즘을 이해해야 함
"""

import time

n = int(input("Number of elements:"))
haystack = [k for k in range(n)]

print("Searching for the maximum value...")

start = time.time()
maximum = max(haystack)
elapsed = time.time() - start

print(f"Maximum element {maximum}, Elapsed time: {elapsed:.2f} seconds")
