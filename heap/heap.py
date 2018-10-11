class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    while (index - 1)//2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1)//2] = self.storage[(index - 1)//2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    pass
