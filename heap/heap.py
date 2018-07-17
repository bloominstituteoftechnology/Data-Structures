class Heap:
  def __init__(self):
    #this is a max heap
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    # store our max val in var so we can return it later
    retval = self.storage[1]
    #replace the first storage element with the last element of the heap
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    # remove the last element from the heap
    self.storage.pop()
    # call sift down to move the element at index 1 down to a value spot on the heap
    self._sift_down(1)
    return retval

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # keep bubbling till reaches valid spot on the heap
    # loop until we no longer have a valid parent index
    while index // 2 > 0:
      #check to see if the element's parent's value is less than the current value
      if self.storage[index // 2] < self.storage[index]:
        # we need to swap them if above is true
        self.storage[index // 2], self.storage[index] = self.storage[index], self.storage[index // 2]
      # our heap element is in the right spot in the heap
      else:
        break
        #update our index value to be the parents index so that we can continue moving up the heap
      index = index // 2



    """index = index-1
    if self.storage[index] > self.storage[index / 2]:
        tmp = self.storage[index]
        self.storage[index] = self.storage[index / 2]
        self.storage[index / 2] = tmp
        self._bubble_up(index / 2)
"""
  def _sift_down(self, index):
    # keep sift element at the given index down the heap until it reaches a valid spot
    while (index * 2) <= self.size:
      # figure out which child is larger
      mc = self._max_child(index)
      # check to see if mc and the current node need to be swapped
      if self.storage[index] < self.storage[mc]:
        # if it is, swap them
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      else:
        break
      # update our index value
      index = mc

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      #return child with the larger value
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1