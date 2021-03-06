"""
1. 총 재생수가 많은 장르 순
2. 장르 내에서 많이 재생된 순
3. 장르 내 재생수 동일한 경우, 고유 번호 낮은 순

=> 장르 별 노래 2개씩 인덱스로 리턴
"""


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.index = None
        self.next = None


class LinkedDict:
    def __init__(self, length):
        self.items = [Node()] * length

    def add(self, key, value, index):
        idx = self.get_idx(key)
        if not self.items[idx]:
            self.items[idx] = [Node(key, value, index)]
            return

        self.items[idx] =
        pass

    def get(self, key):
        idx = self.get_idx(key)
        return self.items[idx].index

    def get_idx(self, key):
        return hash(key) % len(self.items)


def get_melon_best_album(genre_array, play_array):

print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
