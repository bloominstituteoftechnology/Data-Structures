class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        #store value at end of list
        #bubble up value if needed
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
