class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
  #  `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
    pass

  def delete(self):
  #  `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed. 
    pass

  def get_priority(self):
    pass

  def get_size(self):
  #  `get_size` returns the number of elements stored in the heap.
    pass

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

    pass
