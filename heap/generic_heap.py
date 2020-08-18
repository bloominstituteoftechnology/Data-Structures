# python3 heap/test_generic_heap.py -v

class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        self.comparator = comparator
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        last = len(self.storage)-1
        self._bubble_up(last)

    def delete(self):
        if self.size > 1:
            max = self.storage.pop(0)
            self.storage[0], self.storage[len(self.storage)-1] = self.storage[len(self.storage)-1], self.storage[0]
            self.size -=1
            self._sift_down(0)
            return max
        else:
            max = self.storage.pop(0)
            self.size -=1
            return max

    def get_priority(self):
        if self.comparator == None:
            return self.storage[0]
        else:
            return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        if self.comparator == None:
            while index > 0:
                parent = (index - 1) // 2
                if self.storage[index] > self.storage[parent]:
                    self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                    index = parent
                else:
                    break
        else:
           while index > 0:
                parent = (index - 1) // 2
                if self.storage[index] < self.storage[parent]:
                    self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                    index = parent
                else:
                    break

    def _sift_down(self, index):
        if self.comparator == None:
            next = index + 1
            while index < (len(self.storage)-1):
                if next <= (len(self.storage)-1) and self.storage[next] <= self.storage[index]:
                  next += 1
                  self._sift_down(next)
                elif next <= (len(self.storage)-1) and self.storage[next] > self.storage[index]:
                    self.storage[index], self.storage[next] = self.storage[next],self.storage[index]
                    self._sift_down(next)
                    self._sift_down(self.storage[0])
                else:
                    break
        else:
            next = index + 1
            while index < (len(self.storage)-1):
                if next <= (len(self.storage)-1) and self.storage[next] >= self.storage[index]:
                  next += 1
                  self._sift_down(next)
                elif next <= (len(self.storage)-1) and self.storage[next] < self.storage[index]:
                    self.storage[index], self.storage[next] = self.storage[next],self.storage[index]
                    self._sift_down(next)
                    self._sift_down(self.storage[0])
                else:
                    break
 