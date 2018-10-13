class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
      # index is the index of the element that will be moving up the heap
      # keep bubbling the element at the given index up the heap until it reaches a value
        while (index - 1) // 2 >= 0:
          # check to see if the elements parents value is less than the current value
            if self.storage[(index - 1) // 2] < self.storage[index]:
              # swap the values
                self.storage[index], self.storage[(
                    index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
                # update the index to be the parents index so that we can continue moving up
            index = (index-1) // 2

    def _sift_down(self, index):
        while index * 2 + 1 <= len(self.storage) - 1:
          # figure out the larger of the two children
            mc = self._max_child(index)
            # check to see if we need to swap
            if self.storage[index] < self.storage[mc]:
                self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
            index = mc

    def _max_child(self, index):
      # check if the right child index is out of bounds of our storage array
        if index * 2 + 2 > len(self.storage) - 1:
          # return the left child index
            return index * 2 + 1
        else:
          # return the index corresponding to the child node that has the larger value
            return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2
            # python ternary
