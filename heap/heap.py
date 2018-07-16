import math

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    while self.storage[index] > self.storage[math.floor(index / 2)]:
      temp = self.storage[math.floor(index / 2)]
      self.storage[math.floor(index / 2)] = self.storage[index]
      self.storage[index] = temp

  def _sift_down(self, index):
    pass
