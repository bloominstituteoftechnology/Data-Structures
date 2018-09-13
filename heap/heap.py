class Heap:
  def __init__(self):
    # our storage array where all the elements in the heap are stored
    self.storage = []

  def insert(self, value):
    # initially, just put the given value at the end of the storage array
    self.storage.append(value)
    # call bubble_up to get the new element we just inserted into a valid spot in the heap
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    # store our max value in a variable so we can return it later
    retval = self.storage[0]
    # replace the first storage element with the last element in the heap
    self.storage[0] = self.storage[len(self.storage) - 1]
    # remove the last element in the heap
    self.storage.pop()
    # call sift_down in order to move the element at index 0 down to a valid spot in the heap
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # keep bubbling the element at the given index up the heap until it reaches a valid spot
    while (index - 1) // 2 >= 0:
      # check to see if the element's parent's value is less than the current value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        # if it is, swap them
        # self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
        self.storage[index] = self.storage[(index - 1) // 2]
        self.storage[(index - 1) // 2] = self.storage[index]

      # update our index value to be the parent's index so that we can continue moving up the heap
      index = (index - 1) // 2

  def _sift_down(self, index):
    # keep sifting the element at the given index down the heap until it reaches a valid spot
    while index * 2 + 1 <= len(self.storage) - 1:
      # max_child figures out the larger of this node's two children and returns its index in the heap 
      mc = self._max_child(index)
      # check to see if the child is larger than the current node
      if self.storage[index] < self.storage[mc]:
        # if it is, swap them
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      # update our index value to be the child's index so that we can continue moving down the heap
      index = mc

  # helper function to figure out the node with the larger value of the node at the given index
  # returns the index of the larger child node
  def _max_child(self, index):
    # if the right child index is out of bounds of our storage array
    if index * 2 + 2 > len(self.storage) - 1:
      # return the left child index
      return index * 2 + 1
    else:
      # return the index corresponding to the child node that has a larger value
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2




# class Heap:
#   def __init__(self):
#     self.storage = []
#     self.size = 0

#   def insert(self, value):
#     self.storage.append(value)
#     self.size += 1
#     self._bubble_up()

#   def delete(self):
#     pass

#   def get_max(self):
#     return self.storage[0]

#   def get_size(self):
#     return self.size

#   def _bubble_up(self, index):
#     pass

#   def _sift_down(self, index):
#     pass

