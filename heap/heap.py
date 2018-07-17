import math

class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    pass

  def _bubble_up(self, index):
    parent_index = math.floor((index-1)/2)
    parent = self.storage[parent_index]
    child = self.storage[index]

    if parent < child:
        self.storage[parent_index] = child
        self.storage[index] = parent

  def _sift_down(self, index):
    pass