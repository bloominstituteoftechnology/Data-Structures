class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.get_size() - 1)

  def delete(self):
    pass

  def get_max(self):
    return self.storage[self.get_size() - 1]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index] < self.storage[index // 2]:
        temp = self.storage[index // 2]
        self.storage[index // 2] = self.storage[index]
        self.storage[index] = temp
      index = index // 2

  def _sift_down(self, index):
    pass
