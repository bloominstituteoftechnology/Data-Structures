from math import floor

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.size += 1
    self.storage.append(value)
    self._bubble_up(self.size)

  def delete(self):
    if self.size == 0:
      return
    elif self.size == 1:
      self.size -= 1
      deleted = self.storage[1]
      self.storage.pop()
      return deleted
    elif self.size == 2:
      self.size -= 1
      last_num = self.storage[-1]
      deleted = self.storage[1]
      self.storage = [0, last_num]
      self._sift_down(1)
      return deleted
    else:
      self.size -= 1
      last_num = self.storage[-1]
      deleted = self.storage[1]
      self.storage = self.storage[:1] + [last_num] + self.storage[2:-1]
      self._sift_down(1)
      return deleted

  def get_max(self):
    if self.size > 0:
      return self.storage[1]
    else:
      return 0

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    parent_index = floor(index/2)
    parent = self.storage[parent_index]
    child_index = index
    child = self.storage[child_index]

    if parent == 0:
      return
    if parent > child:
      return
    else:
      self.storage[parent_index] = child
      self.storage[child_index] = parent
      return self._bubble_up(parent_index)

  def _sift_down(self, index):
    parent_index = index
    parent = self.storage[parent_index]
    child_left_index = 2*index
    child_right_index = 2*index + 1

    if child_left_index > self.size:
      #no children to test = end of heap
      return
    elif child_right_index > self.size:
      #left child to test only
      child_left = self.storage[child_left_index]
      if parent < child_left:
        self.storage[parent_index] = child_left
        self.storage[child_left_index] = parent
        return
      else:
        return
    else:
      #test both children
      child_left = self.storage[child_left_index]
      child_right = self.storage[child_right_index]
      if parent > child_left and parent > child_right:
        return
      else:
        if child_left > child_right:
          if parent < child_left:
            self.storage[parent_index] = child_left
            self.storage[child_left_index] = parent
            return self._sift_down(child_left_index)
          else:
            return
        else:
          if parent < child_right:
            self.storage[parent_index] = child_right
            self.storage[child_right_index] = parent
            return self._sift_down(child_right_index)
          else:
            return