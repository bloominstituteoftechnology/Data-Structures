import math

class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    if self.get_size() > 1:
        index = self.get_size() - 1
        while index:
            index = self._bubble_up(index)

  def delete(self):
    pass

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_index = math.floor((index-1)/2)
    parent = self.storage[parent_index]
    child = self.storage[index]

    if parent < child:
        self.storage[parent_index] = child
        self.storage[index] = parent
        self.storage[parent_index] = child
        return parent_index
    
    return False

  def _sift_down(self, index):
    pass