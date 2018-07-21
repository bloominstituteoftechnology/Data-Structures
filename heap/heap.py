class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    # append the value to the storage array
    self.storage.append(value)
    #increment the size
    self.size += 1
    # call the bubble_up helper method to put this value in a valid spot in the heap
    # pass the index where this just got added. The index where the value just got appended to the storage list
    self._bubble_up(self.size)

  def delete(self):
    # delete returns the value at the spot in the storage array, but not 0.
    # store our max value in a variable so we can return it later
    return_value = self.storage[1]
    # replace the first storage element with the last element in the heap
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    # remove the last element from the heap
    self.storage.pop()
    # call _sift_down to move the element at index1 to valid spot
    self._sift_down(1)
    return return_value

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.siz

  def _bubble_up(self, index):
    # keep bubbling the element at the given index up the heap until it reached the valid spot
    # run the loop to find the parent of the current index(line 36). As the parent share 2 child nodes that's why divide by 2. // means divide but disregard the remainder. If it hits 0, mean we hit the root.
    while index // 2 > 0: 
      # check to see if the element's parent's value is less than the current value.
      if self.storage[index // 2 < self.storage[index]:
        # we need to swap them
        self.storage[index // 2], self.storage[index] = self.storage[index], self.storage[index // 2]
        # our heap element has reached a valid spot in the heap
      else:
        break
        # update our incex value to be the parent index so that we can continue moving up the heap
      index = index // 2

  def _sift_down(self, index):
    # opposite approach from bubble up
    # keep sifting the element at the given index down the heap until it reach the valid spot
    while (index * 2) <= silf.size:
      # figure out while child is larger
      mc = self._max_child(index)
      # check to see if mc and the current node need to be swapped
      if self.storage[index] < self.storage[mc]:
        # if it is, swap them
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      else:
        break
      #update our index value
      index = mc
  
  # create helper function for sift down to find the max child
  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      # return the child with the larger value
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1

