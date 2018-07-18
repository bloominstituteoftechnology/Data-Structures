class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    # append the value to the storage array
    self.storage.append(value)
    # increment the size
    self.size += 1
    # call bubble_up to put this value in a valid spot
    self._bubble_up(self.size)

  def delete(self):
    # store max value in a var so we can return it later
    retval = self.storage[1]
    # replace the first storage element with the last element in the heap
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    # remove the last element from the heap
    self.storage.pop()
    # call _sift_down to move the element at index 1 down to a valid spot
    self._sift_down(1)
    return retval

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # keep bubbling the element at the given index up the heap until it reaches a valid spot
    # loop until we no longer have a valid parent index
    while index // 2 > 0:
      # check to see if the element's parent's value is less than the current element's value
      if self.storage[index // 2] < self.storage[index]:
        # we need to swap them
        self.storage[index // 2], 
        self.storage[index] = self.storage[index], 
        self.storage[index // 2]
      # our heap element has reached a valid spot in the heap
      else: 
        break
      # update our index value to be the parent's index so we can continue
      index = index // 2

  def _sift_down(self, index):
    # keep sifting the element at the given index down the heap until it reaches a valid spot
    while (index * 2) <= self.size:
      # figure out which child is larger
      mx_chld = self._max_child(index)
      # check to see if mx-chld and the current node need to be swapped
      if self.storage[index] < self.storage[mx_chld]:
        # if it is, swap them
        self.storage[index], self.storage[mx_chld] = self.storage[mx_chld], self.storage[index]
      else:
        break
        # update our index value
        index = mx_chld

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      # return the child with the larger value
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1