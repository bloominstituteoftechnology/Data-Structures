class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    value = self.storage[0]
    # replace the first storage element with the last element in the heap
    self.storage[0] = self.storage[(len(self.storage) - 1)]
    # remove the last element in the heap
    self.storage.pop()
    self._sift_down(0)
    return value

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # index is the index of the element that will be moving up the heap
    # keep bubbling the element at the given index up the heap until it reaches a value equal to zero
    while (index - 1) // 2 >= 0:
    # check to see if the element's parent's value is less than the current value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        # swap values
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      # update the index to be the parent's index so we can continue moving up 
      index = ((index - 1) // 2)

  def _sift_down(self, index):
    # loop runs while left child index is in bounds of total indices in array
    while index * 2 + 1 <= len(self.storage) -1:
    # figure out the larger of the two children
      max_child = self._max_child(index)
      # check if we need to swap
      if self.storage[index] < self.storage[max_child]:
        # swap
        self.storage[index], self.storage[max_child] = self.storage[max_child], self.storage[index]
      index = max_child

    
  def _max_child(self, index):
    # checks if the right child index is out of bounds of our storage array
    if index * 2 + 2 > len(self.storage) -1:
      # return left child index
      return index * 2 + 1
    else:
      # return the index corresponding to the child node that has the larger value
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2




