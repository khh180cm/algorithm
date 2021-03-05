from linked_tuple import LinkedTuple


class LinkedDict:
    def __init__(self):
        self.items = list()
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        idx = self._get_idx(key)
        self.items.append(idx).add(key, value)

    def get(self, key):
        idx = self._get_idx(key)
        return self.items[idx].get(key)

    def _get_idx(self, key):
        return hash(key) % len(self.items)