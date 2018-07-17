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
    if self.size == 0:
      return None
    elif self.size == 1:
      self.size -= 1
      return self.storage.pop()
    else:
      new_node = self.storage.pop()
      old_node = self.storage[1]
      self.storage[1]= new_node
      self.size -= 1
      self._sift_down(1)
      return old_node

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
