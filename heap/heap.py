class Heap:
    def __init__(self):
        self.storage = [0]

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        deleted = self.storage[1]
        self.storage[1] = self.storage[len(self.storage) - 1]
        self.storage.pop()
        self._sift_down(1)
        return deleted

    def get_max(self):
        return self.storage[1]

    def get_size(self):
        return len(self.storage) - 1

    def _bubble_up(self, index):
        while (index // 2) > 0:
            if self.storage[index // 2] < self.storage[index]:
                self.storage[index // 2], self.storage[index] = self.storage[index], self.storage[index // 2]
            else:
                break
            index = index // 2

    def _sift_down(self, index):
        while index * 2 <= len(self.storage) - 1:
            if (index * 2) + 1 > len(self.storage) - 1:
                larger_child = index * 2 
            else:
                if self.storage[index * 2] > self.storage[(index * 2) + 1]:
                    larger_child = index * 2
                else:
                    larger_child = index * 2 + 1

            if self.storage[index] < self.storage[larger_child]:
                self.storage[index], self.storage[larger_child] = self.storage[larger_child], self.storage[index]
            else:
                break
            index = larger_child
