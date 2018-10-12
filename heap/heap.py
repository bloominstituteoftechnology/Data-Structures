class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[-1]
    self.storage.pop()
    self._sift_down(0)
    return retval

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # while parent element's index is greater than 0
    while (index - 1) // 2 >= 0:
      # check to see if the element's parent's value is less than the current value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        # swap the values
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      # update index to be the parent's index so that we can continue moving up the heap
      index = (index - 1) //2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      # figure out the larger of the two children
      mc = self._max_child(index)
      # check to see if we need to swap
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    # check if right child is out of bounds of array
    if index * 2 + 2 > len(self.storage) - 1:
      # return left child index
      return index * 2 + 1
    else:
      # return the index corresponding to the child node that has the larger value
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2 