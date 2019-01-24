class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    return self._bubble_up(self.get_size() - 1)

  def delete(self):
    returnvalue = self.storage[1]
    self.storage[1] = self.storage[self.get_size]
    self.get_size = self.get_size - 1
    self.storage.pop()
    self._sift_down(1)
    return returnvalue

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index] < self.storage[index // 2]:
         tmp = self.storage[index // 2]
         self.storage[index // 2] = self.storage[index]
         self.storage[index] = tmp
      index = index // 2

  def _sift_down(self, index):
    pass
