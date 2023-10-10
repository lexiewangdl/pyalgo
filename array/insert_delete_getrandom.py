# 380. Insert, Delete, GetRandom O(1)
import random


class RandomizedSet:

    def __init__(self):
        self.data = []
        self.data_len = 0
        self.mapping = dict()

    def insert(self, val: int) -> bool:
        if val in self.mapping.keys():
            return False
        self.data.append(val)
        self.mapping[val] = self.data_len
        self.data_len += 1
        return True

    def swap(self, idx1, idx2) -> None:
        temp = self.data[idx1]
        self.data[idx1] = self.data[idx2]
        self.mapping[self.data[idx2]] = idx1
        self.data[idx2] = temp
        self.mapping[temp] = idx2
        return

    def remove(self, val: int) -> bool:
        val_idx = self.mapping.get(val, -1)
        if val_idx == -1:
            return False
        if val_idx != self.data_len - 1:
            self.swap(val_idx, self.data_len - 1)
        self.data.pop(self.data_len - 1)
        self.mapping.pop(val)
        self.data_len -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

