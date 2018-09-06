class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index] < self.storage[index // 2]:
        tmp = self.storage[index // 2]
        self.storage[index // 2] = self.storage[index]
        self.storage[index] = tmp
      index = index // 2

  def _sift_down(self, index):
    while (index * 2) <= self.size:
      mc = self.min_child(index)
      if self.storage[index] > self.storage[mc]:
        tmp = self.storage[index]
        self.storage[index] = self.storage[mc]
        self.storage[mc] = tmp
      index = mc
  
  def min_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      if self.storage[index * 2] < self.storage[index * 2 + 1]:
        return index * 2
      else:
        return index * 2 + 1
