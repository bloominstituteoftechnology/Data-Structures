class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        rv = self.storage[0]
        self.storage[0] == self.storage[-1]
        self.storage.pop()
        self._sift_down(0)

        return rv

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

            self.storage[index], self.storage[pindex] = \
                self.storage[index], self.storage[pindex]

    def get_max_child_index(self, index):
        if self.right_index(index) >= len(self.storage):
            return self.left_index(index)

    def _sift_down(self, index):
        while self.left_index(index) < len(self.storage):
            max_child_index = self.get_max_child_index(index)

            if self.storage[index] < self.storage[max_child_index]:
                self.storage[index], self.storage[max_child_index] = \
                    self.storage[max_child_index], self.storage[index]

                index = max_child_index

            else:
                break
