import math

class Heap:
    def __init__(self):
        self.storage = []
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        index = 0 if self.get_size() == 0 else self.get_size() - 1
        self._bubble_up(index)

    def delete(self):
        # swap root with last node
        root = self.storage[0]
        self.storage[0] = self.storage[self.get_size() - 1]
        self.storage[self.get_size() - 1] = root

        # pop off last node
        max = self.storage.pop(self.get_size() - 1)

        # sift down
        self._sift_down(0)
        return max

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = math.floor((index-1)/2)

        while index != 0 and self.storage[parent_index] < self.storage[index]:
            parent = self.storage[parent_index]
            self.storage[parent_index] = self.storage[index]
            self.storage[index] = parent
            index = parent_index
            parent_index = math.floor((index-1)/2)

    def _sift_down(self, index):
        left_index = self._get_left_index(index)
        right_index = self._get_right_index(index)

        while left_index and self.storage[index] < self.storage[left_index]:
            parent = self.storage[index]
            
            if self.storage[left_index] > self.storage[right_index]:
                self.storage[index] = self.storage[left_index]
                self.storage[left_index] = parent
                left_index = self._get_left_index(left_index)
            else:
                self.storage[index] = self.storage[right_index]
                self.storage[right_index] = parent
                left_index = self._get_left_index(left_index)
                
            right_index = left_index + 1 if left_index else None

    def _get_parent_index(self, index):
        pass

    def _get_left_index(self, index):
        left_index = (2*index) + 1
        return left_index if left_index < self.get_size() else None

    def _get_right_index(self, index):
        right_index = (2*index) + 2
        return right_index if right_index < self.get_size() else None
