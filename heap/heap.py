import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    removed = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.storage.pop()
    self.size -= 1
    if self.size > 0:
      self._sift_down(1)
    return removed

  def get_max(self):
    if self.size > 0:
      return self.storage[1]
    else:
      return 0

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    if index > 1:
      parent_index = math.floor(index/2)
      parent = self.storage[parent_index]
      child = self.storage[index]
      if parent < child:
        self.storage[parent_index] = child
        self.storage[index] = parent
        self._bubble_up(parent_index)

  def _sift_down(self, index):
    parent = self.storage[index]
    fc_index = 2*index
    sc_index = 2*index+1
    if self.size >= sc_index:
      second_child = self.storage[sc_index]
      first_child = self.storage[fc_index]
      if parent < second_child and second_child >= first_child:
        self.storage[sc_index] = parent
        self.storage[index] = second_child
        self._sift_down(sc_index)
      elif parent < first_child and first_child >= second_child:
        self.storage[fc_index] = parent
        self.storage[index] = first_child
        self._sift_down(fc_index)
    elif self.size >= fc_index:
      first_child = self.storage[fc_index]
      if parent < first_child:
        self.storage[fc_index] = parent
        self.storage[index] = first_child
        self._sift_down(fc_index)

