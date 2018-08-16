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
    first_val = self.storage[1]
    last_val = self.storage.pop()
    self.size -= 1
    if self.size == 0:
      return first_val

    self.storage[1] = last_val
    self._sift_down(1)
    return first_val

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    parent_index = index // 2
    if parent_index >= 1 and self.storage[index] > self.storage[parent_index]:
      stored_value = self.storage[index]
      self.storage[index] = self.storage[parent_index]
      self.storage[parent_index] = stored_value
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    if 2*index > self.size: 
      left_index = index
    else:
      left_index = 2*index
    if 2*index+1 > self.size:
      right_index = index
    else:
      right_index = 2*index+1
    if self.storage[left_index] > self.storage[right_index]:
      child_index = left_index
    else:
      child_index = right_index
    if child_index == index:
      return
    if self.storage[child_index] > self.storage[index]:
      stored_value = self.storage[index]
      self.storage[index] = self.storage[child_index]
      self.storage[child_index] = stored_value
      self._sift_down(child_index)