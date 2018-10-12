class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    # replace the first storage element with the last element in the heat(storage array)
    self.storage[0] = self.storage[-1]
    # remove the last element in the heap
    self.storage.pop()
    self._sift_down(0)
    return retval

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index-1)//2] = self.storage[(index -)]
        
  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      # figure out the larger of the two children
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    # check if the right child index is out of bounds of our storage array
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      # return the index corresponding to the child node that has the larger value
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2
