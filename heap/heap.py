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
    self._bubble_up(self.size)

  def delete(self):
    deleted = self.get_max()
    self.storage[1] = self.storage[self.get_size()]
    self.storage.pop()
    self.size -= 1
    self._sift_down(1)
    return deleted

    

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    children = self.storage[index]
    parentIndex = math.floor( (index - 1) / 2 ) + 1
    parent = self.storage[parentIndex]
    if children > parent:
      self.storage[index] = parent
      self.storage[parentIndex] = children
      self._bubble_up(parentIndex)

  def _sift_down(self, index):
    if self.get_size() > 1:
      parent = self.storage[index]
      leftChildIndex = 2 * index
      rightChildIndex = leftChildIndex + 1
      largestIndex =  index
      if leftChildIndex < self.get_size():
        leftChild = self.storage[leftChildIndex]
        if rightChildIndex < self.get_size():
          rightChild = self.storage[rightChildIndex]
        else:
          rightChild = leftChild
        if leftChild >= rightChild: 
          largestIndex = leftChildIndex
        else:
          largestIndex = rightChildIndex

        if parent < self.storage[largestIndex]:
          self.storage[index] = self.storage[largestIndex]
          self.storage[largestIndex] = parent
          self._sift_down(largestIndex)


