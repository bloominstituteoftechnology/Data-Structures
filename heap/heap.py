class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    pass

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        current = self.storage[(index - 1) // 2]
        self.storage[(index - 1) // 2] = self.storage[index]
        self.storage[index] = current
      index = (index - 1) // 2

  def _sift_down(self, index):
    pass
