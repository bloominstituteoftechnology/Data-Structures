class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size()-1)

    def delete(self):
        if self.get_size() == 0:
            return None
        first = self.storage[0]
        end = self.storage.pop()
        if self.get_size() == 0:
            return first
        self.storage[0] = end
        self._sift_down(0)
        return first

    def get_max(self):
        # Will always be the first value in heap
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        index_of_parent = index // 2
        if index_of_parent == 0:
            return
        if self.storage[index_of_parent] < self.storage[index]:
            temp = self.storage[index_of_parent]
            self.storage[index_of_parent] = self.storage[index]
            self.storage[index] = temp
            self._bubble_up(index_of_parent)

    def _sift_down(self, index):
        biggest = None
        while index * 2 + 1 <= len(self.storage) - 1:
            if index*2+2 > len(self.storage)-1:
                biggest = index*2+1
            else:
                biggest = index*2+1 if self.storage[index*2+1] > self.storage[index*2+2] else index*2+2
            if self.storage[index] < self.storage[biggest]:
                self.storage[index], self.storage[biggest] = self.storage[biggest], self.storage[index]
            index = biggest