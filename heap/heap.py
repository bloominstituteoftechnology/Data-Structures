class Node:
    def __init__(self, value=None, L=None, R=None):
        self.value = value
        self.L = L
        self.R = R


class Heap:
    def __init__(self):
        # storage starts with an unused 0 to make
        # integer division simpler later on
        self.storage = [0]
        self.size = 0

    def insert(self, k):
        self.storage.append(k)
        self.size += 1
        self._bubble_up(self.size)

    def delete(self):
        top = self.storage[1]
        self.storage = [0] + self.storage[2:]
        return top

    def get_max(self):
        return self.storage[1]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, i):
        while i // 2 > 0:
            if self.storage[i] > self.storage[i // 2]:
                tmp = self.storage[i // 2]
                self.storage[i // 2] = self.storage[i]
                self.storage[i] = tmp
            i = i // 2
        self.root = self.storage[0]

    def _sift_down(self, i):
        while (i * 2) <= self.size:
            mc = self.maxChild(i)
            if self.storage[i] < self.storage[mc]:
                tmp = self.storage[i]
                self.storage[i] = self.storage[mc]
                self.storage[mc] = tmp
            i = mc

    def maxChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.storage[i * 2] < self.storage[i * 2 + 1]:
                return i * 2 + 1
            else:
                return i * 2
