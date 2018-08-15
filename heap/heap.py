class Heap:
    def __init__(self):
        self.storage = []
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        
        index = self.get_size() - 1
        self._bubble_up(index)

    def delete(self):
        old_root = self.storage[0]
        new_root = self.storage.pop()
        self.size -= 1

        if self.size > 0:
            self.storage[0] = new_root
            index = 0
            self._sift_down(index)

        return old_root

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        while index:
            parent_index = (index-1) // 2
            if self.storage[parent_index] < self.storage[index]:
                self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
                index = parent_index
            else:
                break

    def _sift_down(self, index):
        while index < self.get_size():
            child_index1 = index*2 + 1
            child_index2 = index*2 + 2
            
            if child_index1 >= self.get_size():
                break
            elif child_index2 >= self.get_size():
                larger_child_index = child_index1
            elif self.storage[child_index1] > self.storage[child_index2]:
                larger_child_index = child_index1
            else:
                larger_child_index = child_index2
            
            if self.storage[index] < self.storage[larger_child_index]:
                self.storage[index], self.storage[larger_child_index] = self.storage[larger_child_index], self.storage[index]
                index = larger_child_index
            else:
                break