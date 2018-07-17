class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size = self.size + 1
    self._bubble_up(self.size)

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    index = index-1
    if self.storage[index] > self.storage[index/2]:
        tmp = self.storage[index]
        self.storage[index] = self.storage[index/2]
        self.storage[index/2] = tmp
        self._bubble_up(index/2)

  def _sift_down(self, index):
    pass
