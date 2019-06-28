class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # store value at end of list
        # bubble up value if needed
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        # swap index 0 with last index if needed
        # sift down and pop the new largest node to top
        if len(self.storage) > 1:
            self.swap(0, len(self.storage)-1)
            max = self.storage.pop()
            self._sift_down(0)
        elif len(self.storage) == 1:
            max = self.storage.pop()
        else:
            max = False
        return max

    def get_max(self):
      # A max heap has the highest value at top.
      # this will return the 0 index which is at the top
        return self.storage[0]

    def get_size(self):
      # size is the number of nodes in the list
        return len(self.storage)

    def _bubble_up(self, index):
        # Find parent index
        # if index is at place 0 return it
        # if not swap the values places in the index
        parent = (index-1)//2
        if index <= 0:
            return
        elif self.storage[index] > self.storage[parent]:
            self.swap(index, parent)
            self._bubble_up(parent)

    def _sift_down(self, index):
        # compares values in the heap
        left = (index * 2) + 1
        right = (index * 2) + 2
        max = index

        if len(self.storage) > left and self.storage[max] < self.storage[left]:
            max = left
        if len(self.storage) > right and self.storage[max] < self.storage[right]:
            max = right
        if max != index:
            self.swap(index, max)
            self._sift_down(max)

    # helper function to swap indices
    def swap (self,a,b):
        self.storage[a], self.storage[b] = self.storage[b], self.storage[a]
