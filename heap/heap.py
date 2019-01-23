class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # append value to storage
        self.storage.append(value)
        # bubble up pass in last index
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        pass

    def get_max(self):
        # Max at index 0
        return self.storage[0]

    def get_size(self):
        # return length of storage
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index == 0 and self.storage[parent_index] < self.storage[index]:
            self._swap_indices(parent_index, index)

        if self.storage[parent_index] < self.storage[index]:
            self._swap_indices(parent_index, index)
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        pass

    def _swap_indices(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]
