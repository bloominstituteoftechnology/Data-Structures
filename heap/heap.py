class Heap:
    def __init__(self):
        self.storage = []

    # O(log n)
    def insert(self, value):
        self.storage.append(value)  # O(1)
        self._bubble_up(len(self.storage) - 1)  # O(log n)

    # O(log n)
    def delete(self):
        if len(self.storage) > 1:
            old_value = self.storage[0]  # O(1)
            self.storage[0] = self.storage[-1]  # O(1) to look up in an array
            self.pop()  # O(1) to pop from end of array
            self._sift_down(0)  # O(log n)
            return old_value
        elif len(self.storage == 1):
            return self.storage.pop()  # O(1)

    # O(1)
    def get_max(self):
        return self.storage[0]

    # O(1)
    def get_size(self):
        return len(self.storage)

    # O(log n)
    def _bubble_up(self, index):
        if index < 2:
            return
        # index // 2 will always be parent node
        parent_index = ((index + 1) // 2) - 1
        # if node is larger than parent
        if self.storage[index] > self.storage[parent_index]:
            # swap parent and child - O(1)
            self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            #  increment to prepare for next loop
            parent_index //= 2  # decrementing by half - O(log n)
        return self._bubble_up(parent_index)

    def _sift_down(self, index):
#        first_child_index = index * 2
#        if len(self.storage) < first_child_index + 1:
#            return
        def minChild(self,i):
            if i * 2 + 1 > len(self.storage) - 1:
                return i * 2
            else:
                if self.storage[i*2] < self.storage[i*2+1]:
                    return i * 2
                else:
                    return i * 2 + 1

        while (index * 2) <= len(self.storage) - 1:
            mc = self.minChild(index)
            if self.storage[index] > self.storage[mc]:
                tmp = self.storage[index]
                self.storage[index] = self.storage[mc]
                self.storage[mc] = tmp
            index = mc

    
