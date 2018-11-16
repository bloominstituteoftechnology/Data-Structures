class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        self.storage[0] == self.storage[-1]
        self.storage.pop()
        self._sift_down(0)

    def left_index(self, index):
        return index * 2 + 1

    def left_value(self, index):
        return self.storage[self.left_index(index)]

    def right_index(self, index):
        return index * 2 + 2

    def right_value(self, index):
        return self.storage[self.right_index(index)]

    def parent_index(self, index):
        return (index - 1) // 2

    def parent_val(self, index):
        return self.storage[self.parent_index(index)]

    def get_max(self):
        if len(self.storage) == 0:
            return None

        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0 and self.storage[index] > self.parent_val(index):
            pindex = self.parent_index(index)

            self.storage[index], self.storage[pindex]
            self.storage[index], self.storage[pindex]

    def _sift_down(self, index):
        pass
