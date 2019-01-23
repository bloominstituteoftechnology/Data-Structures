class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.storage[self.size - 1]


  def delete(self):


  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    while (index -1) // 2 >= 0:
        if self.storage[(index -1) // 2] < self.storage[index]:
            self.storage[(index - 1) // 2], self.storage[index] = self.storage[index], self.storage[(index - 1) // 2]
        index = (index - 1) // 2

  def _sift_down(self, index):
    pass
