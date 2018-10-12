import math
class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    parent = math.floor((self.storage.index(value)-1)/2)
    if self.storage[parent] < value:
      return self._bubble_up(parent)

  def delete(self):
    toDelete = self.storage[0]
    if len(self.storage) > 1:
      self.storage[0] = self.storage[-1]
      del self.storage[-1]
      if len(self.storage) == 1:
        return toDelete
      elif len(self.storage) == 2:
        if self.storage[0] < self.storage[1]:
          replace = self.storage[0]
          self.storage[0] = self.storage[1]
          self.storage[1] = replace
      elif self.storage[0] < self.storage[1] or self.storage[0] < self.storage[2]:
        self._sift_down(0)
    else:
      self.storage = []
    return toDelete

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    oldParent = self.storage[index]
    if (2 * index) + 2 > len(self.storage)-1:
      self.storage[index] = self.storage[(2 * index) + 1]
      self.storage[(2 * index) + 1] = oldParent
      if index > 0:
        newParent = math.floor((index-1)/2)
        if self.storage[newParent] < self.storage[index]:
          return self._bubble_up(newParent)
    elif self.storage[(2 * index) + 1] > self.storage[(2 * index) + 2]:
      self.storage[index] = self.storage[(2 * index) + 1]
      self.storage[(2 * index) + 1] = oldParent 
      if index > 0:
        newParent = math.floor((index-1)/2)
        if self.storage[newParent] < self.storage[index]:
          return self._bubble_up(newParent)
    elif self.storage[(2 * index) + 2] > self.storage[(2 * index) + 1]:
      self.storage[index] = self.storage[(2 * index) + 2]
      self.storage[(2 * index) + 2] = oldParent
      if index > 0:
        newParent = math.floor((index-1)/2)
        if self.storage[newParent] < self.storage[index]:
          return self._bubble_up(newParent)
    








  def _sift_down(self, index):
    self.storage = self.storage
    oldParent = self.storage[index]
    if (2 * index) + 2 > len(self.storage)-1:
      self.storage[index] = self.storage[(2 * index) + 1]
      self.storage[(2 * index) + 1] = oldParent
    elif self.storage[(2 * index) + 1] > self.storage[(2 * index) + 2]:
      self.storage[index] = self.storage[(2 * index) + 1]
      self.storage[(2 * index) + 1] = oldParent
      newindex = (2 * index) + 1
      if (2 * newindex) + 1 < len(self.storage) - 1 and self.storage[(2 * newindex) + 1] > self.storage[newindex] or (2 * newindex) + 2 < len(self.storage) - 1 and self.storage[(2 * newindex) + 2] > self.storage[newindex]:
        return self._sift_down(newindex)
    elif self.storage[(2 * index) + 1] < self.storage[(2 * index) + 2]:
      self.storage[index] = self.storage[(2 * index) + 2]
      self.storage[(2 * index) + 2] = oldParent
      newindex = (2 * index) + 2
      if (2 * newindex) + 1 < len(self.storage) - 1 and self.storage[(2 * newindex) + 1] > self.storage[newindex] or (2 * newindex) + 2 < len(self.storage) - 1 and self.storage[(2 * newindex) + 2] > self.storage[newindex]:
        return self._sift_down(newindex)




