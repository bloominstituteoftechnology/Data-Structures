class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # store value at end of list
        # bubble up value if needed
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        # swap index 0 with last index if needed
        # sift down and pop the new largest node to top
        if len(self.storage) > 1:
            self.swap(0,len(self.storage)-1)
            max = self.storage.pop()
            self._sift_down(0)
        elif len(self.storage) == 1:
            max = self.storage.pop()
        else:
            max = False
        return max

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
