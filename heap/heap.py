class Heap:
  def __init__(self):
    self.storage = []
    self.count = 0

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _get_parent(self, index):
    return (index-1)// 2

  def _get_left(self, index):
    left_index = index * 2 + 1
    if left_index > len(self.storage) - 1:
      return None
    else: 
      return left_index

  def _get_right(self, index):
    right_index = index * 2 + 2
    if right_index > len(self.storage) - 1:
      return None
    else: 
      return right_index
    

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc
