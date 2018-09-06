import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) -1)

  def delete(self):
    delVal = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) -1]
    self.storage.pop()
    self._sift_down(0)
    return delVal

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # while (index -1) // 2 >=0:
    #   if self.storage[(index - 1) // 2] < self.storage[index]:
    #     self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index-1) // 2], self.storage[index]
    #   index = (index - 1) // 2

    parent = self.storage[math.floor((index - 1) // 2)]
    child = self.storage[index]
    while parent:
      if child > parent:
        self.storage[math.floor((index - 1) // 2)] = child
        self.storage[index] = parent

  def _sift_down(self, index):
    # while (index * 2 + 1) <= len(self.storage) - 1:
    #   maxChild = self._max_child(index)
    #   if self.storage[index] < self.storage[maxChild]:
    #     self.storage[index], self.storage[maxChild] = self.storage[maxChild], self.storage[index]
    #   index = maxChild


    parent = self.storage[index]
    leftChild = self.storage[2*index + 1]
    rightChild = self.storage[2*index + 2]
    while leftChild:
      if parent < leftChild:
        self.storage[index] = leftChild
        self.storage[2*index + 1] = parent
      elif parent < rightChild:
        self.storage[index] = rightChild
        self.storage[2*index + 2] = parent

  # def _max_child(self, index):
  #   if index * 2 + 2 > len(self.storage) -1:
  #     return index * 2 + 1
  #   else:
  #     return index * 2 + 1 if self.storage[ index * 2 + 1] > self.storage[index * 2 + 2]
