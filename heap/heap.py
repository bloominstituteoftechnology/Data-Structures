class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # add new element at the end of the array
        self.storage.append(value)
        # bubble up until the heap has been reestablished
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        # remove root node
        self.storage.pop(0)
        # move last element to root
        last_element = self.storage.pop()
        self.storage.insert(0, last_element)
        # sift down until the heap has been reestablished
        self._sift_down(0)

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        p_index = (index - 1) // 2

        if index <= 0:
            return

        # if parent node < child node
        if self.storage[p_index] < self.storage[index]:
            # swap positions
            self.storage[index], self.storage[p_index] = (
                self.storage[p_index],
                self.storage[index],
            )

        return self._bubble_up(p_index)

    def _sift_down(self, index):
        pass


heap = Heap()
heap.insert(25)
heap.insert(1)
heap.insert(3)
heap.insert(36)
heap.insert(100)
heap.insert(19)
heap.insert(17)
# print(heap.delete())
print(heap.storage)
