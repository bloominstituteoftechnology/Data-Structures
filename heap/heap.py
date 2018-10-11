class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    # index is index of the element that will be moving up the heap
    # keep bubbling the element at the given index up the heap until it reaches a valid spot
    while (index - 1) // 2 >= 0:
      # check to see if the element's parent's value is less than the current value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        # swap the values
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      # update index to be the parent's index so that we can continue moving up the heap
      index = (index - 1) //2


  def _sift_down(self, index):
    pass # helper function
