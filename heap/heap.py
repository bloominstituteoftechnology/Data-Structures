from math import floor


class Heap:
    def __init__(self):
        self.storage = []
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        self._bubble_up(self.size-1)

    def delete(self):
        if self.size > 0:
            if self.size == 1:
                self.size -= 1
                return self.storage.pop()
            else:
                self.size -= 1
                max, self.storage[0] = self.storage[0], self.storage.pop()
                self._sift_down(0)
                return max
        else:
            return None

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        p_index = floor((index-1) / 2)

        if p_index >= 0 and self.storage[index] > self.storage[p_index]:
            self.storage[p_index], self.storage[index] = (
                self.storage[index], self.storage[p_index])
            self._bubble_up(p_index)

    def _sift_down(self, index):
        l_index = (2 * index) + 1
        l_index = l_index if l_index <= (self.size - 1) else None
        r_index = (2 * index) + 2
        r_index = r_index if r_index <= (self.size - 1) else None
        larger = None

        if l_index is not None:
            if r_index is not None:
                larger = (
                    l_index if self.storage[l_index] > self.storage[r_index]
                    else r_index)
            else:
                larger = l_index
        else:
            larger = r_index if r_index is not None else None

        if larger is not None and self.storage[larger] > self.storage[index]:
            self.storage[index], self.storage[larger] = (
                self.storage[larger], self.storage[index])
            self._sift_down(larger)
