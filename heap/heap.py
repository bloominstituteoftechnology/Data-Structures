class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    # swap first and last value
    self.storage[0], self.storage[len(self.storage) - 1] = self.storage[len(self.storage) - 1], self.storage[0]
    # pop off previous max, store in variable
    prev_max = self.storage.pop
    self._sift_down(0)
    return prev_max

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # while parent element's index is greater than 0
    while (index - 1) // 2 >= 0:
      # check to see if the element's parent's value is less than the current value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        # swap the values
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      # update index to be the parent's index so that we can continue moving up the heap
      index = (index - 1) //2


  def _sift_down(self, index):
    if self.storage[(2 * index) + 1] > self.storage[(2 * index) + 2]: # left greater than right
      if self.storage[(2 * index) + 1] > self.storage[index]: # child greater than parent
        self.storage[index], self.storage[2*index + 1] = self.storage[2*index + 1], self.storage[index] # switch
        index = self.storage[2*index + 1]
    elif self.storage[(2 * index) + 1] < self.storage[(2 * index) + 2]: # right greater than left
      if self.storage[(2 * index) + 1] > self.storage[index]: # child greater than parent
        self.storage[index], self.storage[2*index + 2] = self.storage[2*index + 2], self.storage[index] # switch
        index = self.storage[2*index + 2]
    else: # equal
      if self.storage[(2 * index) + 1] > self.storage[index]: # child greater than parent
        self.storage[index], self.storage[2*index + 1] = self.storage[2*index + 1], self.storage[index] # switch
  


    # # while either child node is greater than the parent
    # while self.storage[(2 * index) + 1] > self.storage[index] or self.storage[(2 * index) + 2] > self.storage[index]:
    #   # if only left_child greater than parent, go left
    #   if self.storage[2*index + 1] > self.storage[index] and self.storage[2*index + 2] < self.storage[index]:
    #     self.storage[index], self.storage[2*index + 1] = self.storage[2*index + 1], self.storage[index]
    #     index = self.storage[2*index + 1]
    #   # if only right_child greater than parent, go right
    #   elif self.storage[2*index + 1] < self.storage[index] and self.storage[2*index + 2] > self.storage[index]:
    #     self.storage[index], self.storage[2*index + 2] = self.storage[2*index + 2], self.storage[index]
    #     index = self.storage[2*index + 2]
    #   # if both child nodes greater than parent, compare child nodes
    #   else:
    #     # if left_child greater than right_child
    #     if self.storage[2*index + 1] > self.storage[2*index + 2]:
    #       self.storage[index], self.storage[2*index + 1] = self.storage[2*index + 1], self.storage[index]
    #       index = self.storage[2*index + 1]
    #     else:
    #       self.storage[index], self.storage[2*index + 2] = self.storage[2*index + 2], self.storage[index]
    #       index = self.storage[2*index + 2]
