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
    self.size += 1

  def delete(self):
    max = self.storage[1]
    self.storage[1] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self.size -= 1
    self._sift_down(1)
    return max

  def get_max(self):
    index = 1 * 2 + 1
    if self.size <= 3:
      return self.storage[1]
    if self.storage[index] > self.storage[1]:
      while True:
        if index > self.size:
          return self.storage[math.floor(index / 2)]
        else:
          if self.storage[index * 2 + 1] > self.storage[index]:
            index = index * 2 + 1
          else:
            return self.storage[index]
    else: 
      return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    parent = math.floor(index / 2)
    if self.storage[index] > self.storage[parent] and self.storage[parent] != 0:
      temp = self.storage[index]
      self.storage[index] = self.storage[parent]
      self.storage[parent] = temp
      self._bubble_up(parent)


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