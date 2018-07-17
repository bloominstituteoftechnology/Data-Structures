class Heap:
    def __init__(self):
# storage starts with an unused 0 to make 
# integer division simpler later on
        self.storage = [0]
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        self._bubble_up(self.size)

# So we want to append the value to the end of the heap. But then we need 
# compare it to its parent until we reach a point where the parent is
# greater than or equal to the value. I think I need to do bubble up first.

    def delete(self):
        max = self.get_max()
        self.storage.pop(0)
        self._sift_down(0)
        return max

    def get_max(self):
        return self.storage[1]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        while index // 2 > 0:
            if self.storage[index] < self.storage[index // 2]:
                temp = self.storage[index // 2]
                self.storage[index // 2] = self.storage[index]
                self.storage[index] = temp
            index = index // 2
# Compare index value with its parent. If parent is < index value, then
# move index value up the heap. 
# Resource: https://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html
    
    def _sift_down(self, index):
        child_index1 = index * 2 + 1
        child_index2 = index * 2 + 2
        newindex = index
        if child_index1 <= self.size - 1 and self.storage[child_index1] > self.storage[child_index2]:
            newindex = child_index1
        if child_index2 <= self.size - 1 and self.storage[child_index2] > self.storage[newindex]:
            newindex = child_index2
        if newindex is not index:
           self.storage[index], self.storage[newindex] = self.storage[newindex], self.storage[index]
