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
        # return len(self.storage)

    def _bubble_up(self, index):
        while (index - 1) // 2 >= 0:
            parent_idx = (index - 1) // 2
            if self.storage[parent_idx] < self.storage[index]:
                self.storage[index], self.storage[parent_idx] = self.storage[parent_idx], self.storage[index]
            index = parent_idx

    def _sift_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index
        if len(self.storage) > left_child and self.storage[largest] < self.storage[left_child]:
            largest = left_child

        if len(self.storage) > right_child and self.storage[largest] < self.storage[right_child]:
            largest = right_child

        if largest != index:
            index, largest = largest, index
            self._sift_down(largest)
