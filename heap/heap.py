class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size = self.size + 1
    self._bubble_up(self.size - 1)

  def delete(self):
    self.storage.pop()

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index // 2 > 0:
      child = self.storage[index]
      parent = self.storage[index // 2]
      if child > parent:
        child = self.storage[index // 2]
        parent = self.storage[index]

  def _sift_down(self, index):
    pass
