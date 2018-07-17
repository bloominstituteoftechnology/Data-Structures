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
        self.storage.shift()
        self._sift_down(0)
        return max

    def get_max(self):
        if self.size > 0:
            self.storage[0] = newroot
            index = 0
            self._sift_down(index)

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        while index // 2 > 0:
            if self.storage[index] > self.storage[index // 2]:
                temp = self.storage[index // 2]
                self.storage[index // 2] = self.storage[index]
                self.storage[index] = temp
                index = index // 2
# Compare index value with its parent. If parent is < index value, then
# move index value up the heap. 
# Resource: https://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html
    
    def _sift_down(self, index):
        if (index * 2 + 1 <= self.size and self.storage[index * 2 + 1] >= self.storage[2 * index]):
            child_index = 2 * index + 1j
        child_index1 = index * 2
        child_index2 = index * 2 + 1
        if self.storage[child_index1] > self.storage[index]:
            temp = self.storage[index]
            self.storage[index] = self.storage[child_index1]
            self.storage[child_index1] = temp
            self._sift_down(child_index)
        if self.storage[child_index2] > self.storage[index]:
            temp = self.storage[index]
            self.storage[index] = self.storage[child_index2]
            self.storage[child_index2] = temp
            self._sift_down(child_index)
