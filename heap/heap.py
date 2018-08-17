from math import floor

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    print('size', self.size)
    self._bubble_up(self.size)
    pass
    
  def delete(self):
    pass

  def get_max(self):
    print(self.storage)
    return self.storage[1]
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    current = self.storage[index]
    parent = self.storage[index // 2]
    if index == 1 or parent >= current:
      return None
    else:
      self.storage[index], self.storage[index // 2] = self.storage[index // 2], self.storage[index]
      self._bubble_up(index // 2)
    pass
