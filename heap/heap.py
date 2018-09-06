class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    node = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.storage.pop()
    self.size -= 1
    self._sift_down(1)
    return node

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while (index // 2) > 0:
      if self.storage[index // 2] < self.storage[index]:
        node = self.storage[index // 2]
        self.storage[index // 2] = self.storage[index]
        self.storage[index] = node
      index = index // 2
  
  def _sift_down(self, index):
    if self.size > 1:
      for i, val in enumerate(self.storage):
        if self.storage[index] < val:
          node = self.storage[index]
          self.storage[index] = val
          self.storage[i] = node
