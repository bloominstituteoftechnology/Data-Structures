class Heap:
    def __init__(self, comparator):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        if self.storage[-1] > value:
            self.storage.append(value)
        else:
            self.storage[len(self.storage)].append(self.storage[-1])
            self.storage[-1].append(value)

    def delete(self):
        pass

    def get_priority(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
