from math import floor

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.size+1)
    self.size += 1
    
  def get_parent_index(self, child_index):
     return self.storage[int((floor(child_index - 1) / 2))]

  def left_child_index(self, parent_index):
    return self.storage[int(parent_index * 2)]

  def right_child_index(self, parent_index):
    return self.storage[int((parent_index * 2) + 1)]

  def delete(self):
    pass

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
      current_value = self.storage[index]
      parent_value = self.get_parent_index(index)
      if parent_value == 0:
        return 
      while parent_value < current_value:
          if current_value > parent_value:
              current_value, parent_value = parent_value, current_value
      return self.storage[index]


  def _sift_down(self, index):
    
    pass
