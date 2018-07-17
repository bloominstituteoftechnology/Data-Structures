class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    pass

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    parent = index // 2
    if self.storage[parent] > 0 and self.storage[index] > self.storage.parent:
      temp = self.storage[index]
      self.storage[index] = self.storage[parent]
      self.storage[parent] = temp
      self._bubble_up(parent)

  def _sift_down(self, index):
    pass
