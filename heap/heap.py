class Heap:
    def __init__(self):
        self.storage = []

# insert the value into the heap
    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        removed_item = self.storage[0]
        del self.storage[0]
        self._sift_down(0)
        return removed_item

    def get_max(self):
        # first number should be the biggest
        return self.storage[0]

    def get_size(self):
        # returns the length of the array
        return len(self.storage)

# moves bigger values up to the base
# called as a helper function in insert
# "bubble up" the newly inserted element to a valid spot in the heap
    def _bubble_up(self, index):
        # we'll use the child to parent formula here
        # loop while the parent index is a valid heap index
        while (index - 1) // 2 >= 0:
            # child has access to parent at this point with this formula
            # compare the child value against it's parent's value
            # if childs value > parent's value
            if self.storage[(index - 1) // 2] < self.storage[index]:
                # swap these two elements via their indeces
                self.storage[index], self.storage[(
                    index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
        # repeat this process until child no longer needs to be swapped with parent
        # update the index to be the parent's index
            index = (index - 1) // 2

# moves smaller values up to the base
# called as a helper function in delete
# "sifts down" the element at the top of the heap
      # helper in delete
    def _sift_down(self, index):
          # while child index is less than last index
        while index * 2 + 1 <= len(self.storage) - 1:
              # if second child is less than the last index
            if index * 2 + 2 > len(self.storage) - 1:
                  # make the first child the max
                maxSize = index * 2 + 1
              # if second child is greater than first child
            elif self.storage[index * 2 + 1] > self.storage[index * 2 + 2]:
                maxSize = index * 2 + 1
            else:
                maxSize = index * 2 + 2

            if self.storage[maxSize] > self.storage[index]:
                self.storage[maxSize], self.storage[index] = self.storage[index], self.storage[maxSize]
            index = maxSize


# [10, 9, 9, 6, 1, 8, 9, 5]

# ----------10
# --------9----9
# ------6--1--5--2
# -----1
