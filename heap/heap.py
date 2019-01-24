class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        last_index = len(self.storage) - 1
        self._bubble_up(last_index)

    def delete(self):
        # Always delete the priority element first
        removed = self.storage[0]
        # take leaf node in priority old spot
        self.storage[0] = self.storage[-1]
        # remove last element
        self.storage.pop()
        # loop
        for i in range(len(self.storage)):
            # check if left child is bigger than right child
            if self.storage[2*i + 1] > self.storage[2*i + 2]:
                # swap
                temp = self.storage[0]
                self.storage[0] = self.storage[2*i + 1]
                self.storage[2*i + 1] = temp
            else:
                # swap
                temp = self.storage[0]
                self.storage[0] = self.storage[2*i + 2]
                self.storage[2*i + 2] = temp
        # check children
        # swap with larger element
        # if null stop
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
        if left_idnex > self.count - 1:
            return None
        else:
            return this.storage[left_index]

    def _get_right(self, index):
        right_index = index * 2 + 2
        if left_idnex > self.count - 1:
            return None
        else:
            return this.storage[right_index]

    def _bubble_up(self, index):
        parent_index = self._get_parent_index(index)
        # move element at index up the heap if parent value is smaller
        if self.storage[index] > self.storage[parent_index]:
            # swap
            temp = self.storage[parent_index]
            self.storage[parent_index] = self.storage[index]
            self.storage[index] = temp
        # return new index
        return parent_index

    def _sift_down(self, index):
        # grab indecies of element's children
        # if left child is larger or right child is larger
        # check if larger value is bigger than parent
        # if so swap
        pass


heap = Heap()
heap.insert(15)
heap.insert(9)
heap.insert(100)
heap.insert(101)
print(heap.storage)
