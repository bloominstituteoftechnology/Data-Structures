import math

class Heap:
    #TODO: Utilize size property -- this is never updated during insert/delete
    #TODO: Utilize python's built in method for list swapping
    #TODO: Can refactor sift down further
    def __init__(self):
        self.storage = []
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        index = 0 if self.get_size() == 0 else self.get_size() - 1
        self._bubble_up(index)

    def delete(self):
        self._swap(0, self.get_size() - 1)
        max = self.storage.pop(self.get_size() - 1)
        self._sift_down(0)
        return max

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = self._get_parent_index(index)

        while index and self.storage[parent_index] < self.storage[index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = self._get_parent_index(index)

    def _sift_down(self, index):
        left_index = self._get_left_index(index)
        right_index = self._get_right_index(index)

        while left_index and self.storage[index] < self.storage[left_index]:
            if self.storage[left_index] > self.storage[right_index]:
                self._swap(index, left_index)
                left_index = self._get_left_index(left_index)
            else:
                self._swap(index, right_index)
                left_index = self._get_left_index(left_index)
                
            right_index = left_index + 1 if left_index else None

    def _get_parent_index(self, index):
        return math.floor((index-1)/2)

    def _get_left_index(self, index):
        left_index = (2*index) + 1
        return left_index if left_index < self.get_size() else None

    def _get_right_index(self, index):
        right_index = (2*index) + 2
        return right_index if right_index < self.get_size() else None
    
    def _swap(self, src_index, dst_index):
        src = self.storage[src_index]
        self.storage[src_index] = self.storage[dst_index]
        self.storage[dst_index] = src
