class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
  #  `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
  
  # add value to heap
      self.storage.append(value)
  # call bubble up to give heap proper priority
      self._bubble_up(len(self.storage) -1)


  def delete(self):
  #  `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed. 

    # if nothing in heap then return false
    if self.storage == False:
      top = False

    # if Only 1 node in heap delete the value
    elif len(self.storage) == 1:
      top = self.storage.pop()

    # Check to see if self.storage has more than 1 node
    elif len(self.storage) > 1:
    # swap top index in heap with the last index    
      self.storage[0], self.storage[len(self.storage)-1] = self.storage[len(self.storage)-1], self.storage[0]
      # pop value removing it from heap
      top = self.storage.pop()
      # Run sift down to get a new max at top of heap
      self._sift_down(0)
    else:
      top = False
    return top

  def get_max(self):
  #  `get_max` returns the maximum value in the heap _in constant time_.
    return self.storage[0]

  def get_size(self):
  #  `get_size` returns the number of elements stored in the heap.
    return len(self.storage)

  def _bubble_up(self, index):
  #  `_bubble_up` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
    while index > 0:
      # Get parent index
      parent = (index - 1) // 2
    # compare the child against the parent value
    # if child's value is higher priority than it's parent
      if self.storage[index] > self.storage[parent]:
      # swap
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
    # update child's index to be new index
        index = parent
    # otherwise, child is at a valid spot
      else:
      #stop 
        break

  def _sift_down(self, index):
  #  `_sift_down` grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.
    
  # Start with formulas
    left = (index * 2) + 1
    right = (index * 2) + 2
    max = index

    # Check left side
    if len(self.storage) > left and self.storage[max] < self.storage[left]:
      max = left
    # Check right side
    if len(self.storage) > right and self.storage[max] < self.storage[right]:
      max = right
    if max != index:
      # swap values
      self.storage[index], self.storage[max] = self.storage[max], self.storage[index]
    # Recursion to keep going through values
      self._sift_down(max)
