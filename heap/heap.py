class Heap:
    def __init__(self):
        self.storage = []
        self.count = 0

    def insert(self, value):
        self.storage.append(value)
        self.count += 1
        self._bubble_up(self.count - 1)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _get_parent(self, index):
        return self.storage[(index - 1) // 2]

    def _get_left(self, index):
        left_index = index * 2 + 1
        if left_index > self.count - 1:
            return None
        else:
            return self.storage[left_index]

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
