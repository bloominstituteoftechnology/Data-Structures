import math

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    if len(self.storage) == 1:
      return None
    max = self.storage[1]

    self.storage[1] = self.storage[self.size]
    self.size -= 1
    self.storage.pop()
    self._sift_down(1)
    return max

  def get_max(self):
    return self.storage[1]
  
  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while index // 2 > 0:

      if self.storage[index] > self.storage[index // 2] and self.storage[index // 2]:
        # swap them around via array destructuring:
        self.storage[index // 2], self.storage[index] = self.storage[index], self.storage[index // 2]
      else:
        # break out if element has reached the correct spot
        break
      index = index // 2

  def _sift_down(self, index):
    
    while (index * 2) <= self.size:
      mc = self._max_child(index)
      
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      else:
        break

      index = mc

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      return index * 2 if self.storage[index * 2] > self.storage[2 * index + 1] else index * 2 + 1