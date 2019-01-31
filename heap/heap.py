class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
      self.storage.append(value)
      self._bubble_up(self.storage[-1])
    
  def delete(self):
    if len(self.storage) != 0:
      del_element = self.storage[0]
      del(self.storage[0])
      self._sift_down(0)
    return del_element

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_index = (index-1)//2
    last_element = self.storage[-1]
    while parent_index >= 0:
      if last_element > parent_index:
        last_element = parent_index

  

  def _sift_down(self, index):
    pass
    # left_child_idx = (2*index) + 1
    # right_child_idx = (2*index) + 2
    # if 