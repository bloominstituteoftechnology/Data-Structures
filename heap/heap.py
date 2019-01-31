class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    deleted = self.storage[0]
    del(self.storage[0])
    self._sift_down(0)
    return deleted

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[(index - 1) // 2], self.storage[index] = self.storage[index], self.storage[(index - 1) // 2]
      index = (index - 1) // 2
      
  def _sift_down(self, index):
    while index  * 2 + 1 <= len(self.storage) - 1:
      if index * 2 + 2 > len(self.storage) - 1:
        maximum = index * 2 + 1
      elif self.storage[index * 2 + 1] > self.storage[index * 2 + 2]:
        maximum = index * 2 + 1
      else:
        maximum = index * 2 + 2
      
      if self.storage[maximum] > self.storage[index]:
        self.storage[maximum], self.storage[index] = self.storage[index], self.storage[maximum]
      index = maximum
