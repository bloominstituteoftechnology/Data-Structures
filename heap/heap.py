class Heap:
  def __init__(self):
    self.storage = []

# bubble the values from the end up to the start through the length of the array/list
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    pass

  def get_max(self):
   return self.storage[0]
# just the length of the array/list
  def get_size(self):
    return len(self.storage)
    

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
