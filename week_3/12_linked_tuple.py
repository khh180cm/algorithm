"""
링크드 튜플 구현
해쉬 충돌 시, 링크드 튜플 및 리스트 사용
"""


class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v
