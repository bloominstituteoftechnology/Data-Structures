class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        i = (len(self.storage)-1)
        self.storage.append(value)
        self._bubble_up(i)

    def delete(self):
        rv = self.storage.pop(0)
        self._sift_down(0)
        return rv

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index): 
        while index > 0:
            if self.storage[(index-1)//2] < self.storage[index]:
                self.swap((index-1)//2, index)
            index = (index-1)//2

    def _sift_down(self, index):
        left = (2*index)+1
        right = (2*index)+2
        if left<self.get_size() and self.storage[left] > self.storage[index]:
            self.swap(left, index)
            self._sift_down(left)
        if right<self.get_size() and self.storage[right] > self.storage[index]:
            self.swap(right, index)
            self._sift_down(right)

    def swap(self, i, j):
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    # left: 2i + 1 for delete
    # right: 2i + 2 for delete
    # for delete take last node and move to root, then use left/right
    # parent: (i-1)//2 for insert