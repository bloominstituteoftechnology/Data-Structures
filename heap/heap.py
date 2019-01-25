class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # Append the value to the end of the storage
    # Bubble that value up through the heap until
    self.storage.append(value)
    self._bubble_up(self.get_size() - 1)

  def delete(self):
    self.storage[:1], self.storage[-1:] = self.storage[-1:], self.storage[:1]
    self.storage.pop()
    print(self.storage)
    self._sift_down(0)
    print(self.storage)

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)
  
  def _get_parent(self, index):
    return self.storage[(index - 1) // 2]
  
  def _get_right_child(self, index):
    r = index * 2 + 2
    return self.storage[r]
  
  def _get_left_child(self, index):
    l = index * 2 + 1
    return self.storage[l]

  def _bubble_up(self, index):
    parent = self._get_parent(index)
    parent_index = (index - 1) // 2
    while parent_index >= 0:
      if self.storage[index] > parent:
        self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
      parent_index -= 2
        
  
  def _sift_down(self, index):
    for i in range(0, 4):
      current = self.storage[index]
      left_index = (index * 2) + 1
      right_index = (index * 2) + 2
      if self._get_left_child(index) is not None:
        if current < self._get_left_child(index):
          self.storage[index], self.storage[left_index] = self.storage[left_index], self.storage[index]
          index = left_index
      elif self._get_right_child(index) is not None:
        if current < self._get_right_child(index):
          self.storage[index], self.storage[right_index] = self.storage[right_index], self.storage[index]
          index = right_index