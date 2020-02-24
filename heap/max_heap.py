class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(-1)

    def delete(self):
        # swap first and last
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        current_max = self.storage.pop()
        # sift down new root
        if self.get_size():
            self._sift_down(0)
        return current_max

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # allow negative index
        if index < 0:
            index += self.get_size()
        # compare with parent, and swap if bigger
        parent = (index-1)//2
        if self.storage[index] > self.storage[parent]:
            self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
            # if not index 0, keep bubbling
            if parent:
                self._bubble_up(parent)

    def _sift_down(self, index):
        # allow negative index
        if index < 0:
            index += self.get_size()
        # compare children and swap if smaller
        index_a = 2*index + 1
        index_b = 2*index + 2
        parent = self.storage[index]
        child_a = None
        try:
            child_a = self.storage[index_a]
            child_b = self.storage[index_b]
        except IndexError:
            if child_a and child_a > parent:
                self.storage[index], self.storage[index_a] = self.storage[index_a], self.storage[index]
                self._sift_down(index_a)
            return
        if child_a >= child_b:
            if child_a > parent:
                self.storage[index], self.storage[index_a] = self.storage[index_a], self.storage[index]
                self._sift_down(index_a)
                return
        else:
            if child_b > parent:
                self.storage[index], self.storage[index_b] = self.storage[index_b], self.storage[index]
                self._sift_down(index_b)
                return
