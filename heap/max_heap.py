class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1) # last index to bubble up.

  def delete(self):
    old_top = self.storage[0]
    self.storage[0] = self.storage[-1]  # swap last element to top
    del self.storage[-1]
    self._sift_down(0)

    return(old_top)

  def get_max(self):
    return(self.storage[0])

  def get_size(self):
    return(len(self.storage))

  def _bubble_up(self, index):
    # keep bubbling up until we've either reached the top of the heap
    # or we've reached a point where the parent is higher prio
    while index > 0:
    # on a single bubble up iteration
    # get the parent index 
      parent = (index - 1) // 2
    # compare the child against the value of the parent
    # if the child's value is higher prio than its parent's value
      if self.storage[index] > self.storage[parent]:
      # swap them
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
      # update the child's index to be the new index it is now at
        index = parent
    # otherwise, child is at a valid spot
      else:
      # stop bubbling up
        break

  def _sift_down(self, index):
    '''
          A     # parent A must be larger than its children
        B   C   # if A is smaller than B or C, then A will swap with the larger of children
      D E   F G # if A has swapped with B and B is smaller than D, then B will swap with D.
    '''
    parent = index
   
    while (parent + (2 * index + 2)) <= (len(self.storage)-1)   :
      left_child = (2 * index + 1)
      right_child = (2 * index + 2)
      
      if self.storage[left_child] > self.storage[right_child]:
        larger_child = left_child
      else:
        larger_child = right_child

      if self.storage[larger_child] > self.storage[parent]:
        self.storage[larger_child], self.storage[parent] = self.storage[parent], self.storage[larger_child]
        parent = larger_child
        index += 1
      else:
        break





