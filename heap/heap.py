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
    return len(self.storage)

  def _bubble_up(self, index):
    parent = floor((index - 1)/2)
    if self.storage[index] > parent:
      parent = self.storage[index]

  def _sift_down(self, index):
    pass
