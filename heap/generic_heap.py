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
        if self.size == 0:
            return None

        storage_top = self.storage[1]
        storage_end = self.storage.pop()

        self.size -= 1

        if self.size == 0:
            return storage_top

        self.storage[1] = storage_end

        self._sift_down(1)

        return storage_top

    def get_priority(self):
        pass

    def get_size(self):
        return self.size

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
        index_left = index if 2 * index > self.size else 2 * index

        index _right = index if 2 * index + 1 > self.size else 2 * index + 1

        index_of_child = index_left if self.storage[index_left] > self.storage[index_right] else index_right

        if index_of_child == index:
            return

        if self.storage[index_of_child] > self.storage[index]:
            temp = self.storage[index]
            self.storage[index] = self.storage[index_of_child]
            self.storage[index_of_child] = temp
            self._sift_down(index_of_child)
