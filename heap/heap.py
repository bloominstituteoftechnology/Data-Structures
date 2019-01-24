class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    old_max = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return old_max

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[(index - 1) // 2], self.storage[index] = self.storage[index], self.storage[(index -1) // 2]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      max_child = self._max_child(index)
      if self.storage[index] < self.storage[max_child]:
        self.storage[index], self.storage[max_child] = self.storage[max_child], self.storage[index]
      index = max_child

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      if self.storage[index * 2 + 1] > self.storage[index * 2 + 2]:
        return index * 2 + 1
      else:
        return index * 2 + 2

