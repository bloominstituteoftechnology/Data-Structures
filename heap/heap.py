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
    # call the bubble_up helper method to put this value in a valid spot in the heap
    self._bubble_up(self.size) 

  def delete(self):
    # store our max value in a variable so we can return it later
    retval = self.storage[1]
    # replace the first storage element with the last element in the heap
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    # remove the last element from the heap
    self.storage.pop() 
    # call _sift_down to move the element at index 1 down to a valid spot in the heap
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
      # check to see if the element's parents value is less than the current value 
      if self.storage[index // 2] < self.storage[index]: 
        # we need to swap them 
        self.storage[index // 2], self.storage[index] = self.storage[index], self.storage[index // 2]
        # our heap element has reached a valid spot in the heap
      else: 
        break
      # update our index value to be the parent's index so that we can continue moving up the heap
      index = index // 2

  def _sift_down(self, index):
    # keep sifting the element at the given index down the heap until it reaches a valid spot
    while (index * 2) <= self.size: 
      # figure out which child is larger 
      mc = self._max_child(index)
      # check to see if mc and the current node need to be swap
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
      # return the child with the larger value 
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1
