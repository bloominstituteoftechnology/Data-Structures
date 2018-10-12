class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    index = len(self.storage) - 1
    self.storage.append(value)
    self._bubble_up(index)
    
  def delete(self):
    element = self.storage.pop(0)
    self._sift_down(0)
    return element

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    left_child = (2*index) + 1
    right_child = (2*index) + 2
    if left_child < self.get_size() and right_child < self.get_size():
      if self.storage[left_child] < self.storage[right_child]:
        child = right_child
      else:
        child = left_child
      if self.storage[child] > self.storage[index] and child < self.get_size():
        self.storage[child], self.storage[index] = self.storage[index], self.storage[child]
        return self._sift_down(child)
    # if left_child < self.get_size() and self.storage[left_child] > self.storage[index]:
    #   self.storage[left_child], self.storage[index] = self.storage[index], self.storage[left_child]
    #   self._sift_down(left_child)
    # if right_child < self.get_size() and self.storage[right_child] > self.storage[index]:
    #   self.storage[right_child], self.storage[index] = self.storage[index], self.storage[right_child]
    #   self._sift_down(right_child)

