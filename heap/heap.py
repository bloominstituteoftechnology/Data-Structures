import math

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size = self.size + 1
    self._bubble_up(self.size)

  def delete(self):
    deleted_value = self.storage.pop(0)
    self.size -= 1
    self._sift_down(0)
    return deleted_value

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while index > 0:
      if self.storage[index] > self.storage[index // 2]:
         tmp = self.storage[index // 2]
         self.storage[index // 2] = self.storage[index]
         self.storage[index] = tmp
      index = index // 2

  def _sift_down(self, index):
    if len(self.storage) > 1:
      for i, val in enumerate(self.storage):
        if self.storage[index] < val:
          temp = self.storage[index]
          self.storage[index] = val
          self.storage[i] = temp