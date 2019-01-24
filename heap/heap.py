class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        return self._bubble_up(self.get_size() - 1)

    def delete(self):
        pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        storage = self.storage
        if index == 0:
            return
        if storage[(index - 1)//2] > storage[index]:
            return
        elif storage[(index-1)//2] < storage[index]:
            storage[(index-1) //
                    2], storage[index] = storage[index], storage[(index - 1)//2]
            return self._bubble_up((index - 1)//2)

    def _sift_down(self, index):
        pass
