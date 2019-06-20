class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)  # add new value to the end of the heap
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if self.storage[0]:
            return self.storage.pop(0)
        self._bubble_up(len(self.storage)-1)

    def get_max(self):
        if len(self.storage) > 0:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent
            else:
                break

    def _sift_down(self, index):
        pass
