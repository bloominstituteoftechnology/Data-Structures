class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[]

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      #figure out the larger of the two children
      mac_child = self._max_child(index)
      # check to seee if we need to swap
      if self.storage[index] < self.storage[mac_child]:
        self.storage[index], self.storage[mac_child] = self.storage[mac_child], self.storage[index]

  def _max_child(self, index)
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self
