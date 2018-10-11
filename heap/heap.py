class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        if self.get_size() == 1:
            return self.storage.pop()
        temp = self.storage[0]
        self.storage[0] = self.storage.pop()
        self._sift_down(0)
        return temp

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index//2 >= 0:
            if index == 0:
                break
            elif self.storage[index] > self.storage[index//2]:
                self.storage[index], self.storage[index//2] = self.storage[index//2], self.storage[index]
            else:
                break
            index = index // 2

    def _sift_down(self, index):
        while index * 2 + 1 <= self.get_size() - 1:
            if index * 2 + 2 > self.get_size() - 1:
                max_child = index * 2 + 1
            else:
                max_child = index * 2 + 1 if self.storage[index*2+1] > self.storage[index*2 + 2] else index * 2 + 2
            if self.storage[max_child] > self.storage[index]:
                self.storage[max_child], self.storage[index] = self.storage[index], self.storage[max_child]
            else:
                break

            index = max_child
