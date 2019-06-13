class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        pass

    def _bubble_up(self, index):
        while (index - 1) // 2 >= 0:
            parent_idx = (index - 1) // 2
            if self.storage[parent_idx] < self.storage[index]:
                self.storage[index], self.storage[parent_idx] = self.storage[parent_idx], self.storage[index]
            index = parent_idx

    def _sift_down(self, index):
        pass
