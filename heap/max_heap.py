class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        k = 0
        while (2*k + 2) <= len(self.storage):
            if value > self.storage[k]:
                self.storage.insert(k, value)
                break

            elif self.storage[2*k + 1] > self.storage[2*k + 2]:
                if value > self.storage[2*k + 1]:
                    self.storage.insert(2*k + 1, value)

            elif self.storage[2*k + 1] <= self.storage[2*k + 2]:
                if value > self.storage[2*k + 2]:
                    self.storage.insert(2*k + 2, value)

        k += 1

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        while (index - 1) // 2 >= 0:
            if self.storage[(index - 1) // 2] < self.storage[index]:
                self.storage[index], self.storage[(
                    index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
            index = (index - 1) // 2

    def _sift_down(self, index):
        pass
