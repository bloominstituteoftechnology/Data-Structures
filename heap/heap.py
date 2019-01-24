class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # Add value to storage
        self.storage.append(value)
        # save index in value
        last_index = len(self.storage) - 1
        # make heap valid
        self._bubble_up(last_index)

    def delete(self):
        # Always delete the priority element first
        removed = self.storage[0]
        # take leaf node in priority old spot
        self.storage[0] = self.storage[-1]
        # remove last element
        self.storage.pop()
        # sift down
        self._sift_down(0)

        return removed

    def get_max(self):
        if self.storage[0]:
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _get_parent_index(self, index):
        return (index - 1) // 2

    def _get_left(self, index):
        left_index = index * 2 + 1
        if left_index > len(self.storage) - 1:
            return None
        else:
            return left_index

    def _get_right(self, index):
        right_index = index * 2 + 2
        if right_index > len(self.storage) - 1:
            return None
        else:
            return right_index

    def _bubble_up(self, index):
        while index > 0:
            parent_index = self._get_parent_index(index)
            # move element at index up the heap if parent value is smaller
            if self.storage[index] > self.storage[parent_index]:
                # swap
                temp = self.storage[parent_index]
                self.storage[parent_index] = self.storage[index]
                self.storage[index] = temp
                index = parent_index
            else:
                return

    def _sift_down(self, index):
        # check if left child is bigger than right child
        while 2*index + 2 <= len(self.storage) - 1:
            if self.storage[2*index + 1] >= self.storage[2*index + 2]:
                if self.storage[index] <= self.storage[2*index + 1]:
                    # swap
                    temp = self.storage[index]
                    self.storage[index] = self.storage[2*index + 1]
                    self.storage[2*index + 1] = temp
                    index = 2*index + 1
            elif self.storage[2*index + 1] <= self.storage[2*index + 2]:
                if self.storage[index] <= self.storage[2*index + 2]:
                    # swap
                    temp = self.storage[index]
                    self.storage[index] = self.storage[2*index + 2]
                    self.storage[2*index + 2] = temp
                    index = 2*index + 2
            else:
                return


heap = Heap()
heap.insert(6)
heap.insert(8)
heap.insert(10)
heap.insert(9)
heap.insert(1)
heap.insert(9)
heap.insert(9)
heap.insert(5)
print(heap.storage)
# should delete 101 and put 9 in front and delete 9 from end
heap.delete()
print(heap.storage)
