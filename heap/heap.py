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
      index = index //2


  def _sift_down(self, index):
    left_child = index * 2
    right_child = index * 2 + 1
    if self.size == 2:
      if self.storage[1] < self.storage[2]:
        temp = self.storage[1]
        self.storage[1] = self.storage[2]
        self.storage[2] = temp
    if left_child > self.size - 1 and right_child > self.size - 1:
      return
    root = self.storage[index]
    if root < self.storage[left_child] and self.storage[right_child] >= self.storage[left_child]:
      temp = root
      self.storage[index] = self.storage[right_child]
      self.storage[right_child] = temp
      self._sift_down(right_child)
    elif root < self.storage[left_child] and self.storage[right_child] < self.storage[left_child]:
      temp = root
      self.storage[index] = self.storage[left_child]
      self.storage[left_child] = temp
      self._sift_down(left_child)
    if right_child > self.size and root < self.storage[left_child]:
      temp = root
      self.storage[index] = self.storage[left_child]
      self.storage[left_child] = temp
      self._sift_down(left_child)