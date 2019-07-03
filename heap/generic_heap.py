class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_priority(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    parent_index = index
    left = parent_index * 2 +1
    right = parent_index * 2 + 2

    maxIndex = left if self.storage[left] > self.storage[right] else right

    while self.storage[parent_index] < self.storage[maxIndex]:
      temp = self.storage[parent_index]
      self.storage[parent_index] = self.storage[maxIndex]
      self.storage[maxIndex] = temp

      parent_index = maxIndex
      left = parent_index * 2 +1
      right = parent_index * 2 + 2 

