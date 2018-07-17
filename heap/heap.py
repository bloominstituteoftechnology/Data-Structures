class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    # store max value in variable so we can return it later
    retval = self.storage[1]
    # replace the first storage element with the last element in the heap
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    # remove last element from heap
    self.storage.pop()
    # call sift out to move the element at index 1 down to a valid spot
    self._sift_down(1)
    return retval

    # self.storage = self.storage[-1]
    # pass

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # keep bubbling the element at the given index
    # loop until we no longer have a valid parent index
    while index // 2 > 0:
      # check if the element's parent's 
      if self.storage[index // 2] < self.storage[index]:
        self.storage[index // 2], self.storage[index] = self.storage[index], self.storage[index // 2]
      else:
        break
        index = index // 2

  def _sift_down(self, index):
    while (index ** 2) <= self.size:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      else:
        break
      index = mc

  def _max_child(index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      return index * 2  if self.storage[index * 2 ] > self.storage[index * 2 + 1]
