class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)
        print(self.storage)

    def delete(self):
        deleted = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        self.storage.pop()
        self._sift_down(0)
        return deleted

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while (index - 1) // 2 >= 0:
            if self.storage[(index - 1) // 2] < self.storage[index]:
                self.storage[index], self.storage[(
                    index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
            index = (index - 1) // 2

    def _sift_down(self, index):
        while index * 2 + 1 <= len(self.storage) - 1:
            if index * 2 + 2 > len(self.storage) - 1:
                biggest_child = index * 2 + 1
            else:
                biggest_child = index * 2 + \
                    1 if self.storage[index * 2 +
                                      1] > self.storage[index * 2 + 2] else index * 2 + 2
            if self.storage[index] < self.storage[biggest_child]:
                self.storage[index], self.storage[biggest_child] = self.storage[biggest_child], self.storage[index]
            index = biggest_child
