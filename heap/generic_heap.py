class Heap:
    def __init__(self, comparator):
        self.storage = []
        self.comparator = comparator
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        self._bubble_up(self.size)

    def delete(self):
        pass

    def get_priority(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        index_of_parent = index//2
        if index_of_parent == 0:
            return

        if self.storage[index_of_parent] < self.storage[index]:
            temp = self.storage[index_of_parent]
            self.storage[index_of_parent] = self.storage[index]
            self.storage[index] = temp
            self._bubble_up(index_of_parent)

    def _sift_down(self, index):
        pass
