import math


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        root = self.storage[0]
        newRoot = self.storage.pop()
        if self.get_size() > 0:
            self.storage[0] = newRoot
            self._sift_down(0)
        return root

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent = int(math.floor((index - 1) / 2))
        if self.storage[index] > self.storage[parent]:
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
            if parent is not 0:
                self._bubble_up(parent)
            return

    def _sift_down(self, index):
        lChild = (2 * index) + 1
        if lChild > self.get_size() - 1:
            return
        rChild = lChild + 1
        if rChild > self.get_size() - 1:
            return

        if self.storage[index] < self.storage[lChild]:
            self.storage[index], self.storage[lChild] = self.storage[lChild], self.storage[index]
            self._sift_down(lChild)
        if self.storage[index] < self.storage[rChild]:
            self.storage[index], self.storage[rChild] = self.storage[rChild], self.storage[index]
            self._sift_down(rChild)
