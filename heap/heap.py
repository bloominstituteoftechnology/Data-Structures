class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    item = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    self.storage.pop()
    self._sift_down(1)
    return item

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while (index // 2) > 0:
      if self.storage[index // 2] < self.storage[index]:
        tmp = self.storage[index // 2]
        self.storage[index // 2] = self.storage[index]
        self.storage[index] = tmp
      index = index // 2

  def _sift_down(self, index):
    if self.size > 1:
      for i, val in enumerate(self.storage):
        if self.storage[index] < val:
          item = self.storage[index]
          self.storage[index] = val
          self.storage[i] = item
