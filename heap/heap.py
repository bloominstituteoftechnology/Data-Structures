import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    if len(self.storage) != 1:
      curr_index = len(self.storage) - 1
      parent_index = None
      stop_loop = False
      while stop_loop == False:
        parent_index = math.floor((curr_index-1)/2)
        if self.storage[parent_index] < value:
          self.storage.insert(parent_index, value)
          self.storage.pop(curr_index)
          curr_index = parent_index
        if parent_index == 0:
          stop_loop = True

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1 // 2)] < self.storage[index]:

        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]

      index = (index - 1) // 2

  def _sift_down(self, index):
    pass
