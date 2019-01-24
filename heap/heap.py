class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    curr_index = len(self.storage) - 1
    self._bubble_up(curr_index)

  def delete(self):
    val = self.storage[0]
    del self.storage[0]
    print(val)
    self._sift_down(0)
    return val

  def _get_parent(self, index):
    return int((index/2) - 1)

  def _get_right(self, index):
    return int((index * 2) + 2)

  def _get_left(self, index):
    return int((index * 2) + 1)

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_index = self._get_parent(index + 1)
    while self.storage[index] > self.storage[parent_index] and parent_index >= 0:
      temp = self.storage[parent_index]
      self.storage[parent_index] = self.storage[index]
      self.storage[index] = temp
      index = parent_index
      parent_index = self._get_parent(index)

  def _sift_down(self, index):
    next_node = 0
    while next_node * 2 + 1 <= len(self.storage) - 1:
      print(self.storage)
      curr_left = self._get_left(index)
      curr_right = self._get_right(index)
      if curr_right > (len(self.storage) - 1):
        next_node = curr_left
      elif self.storage[curr_left] > self.storage[curr_right]:
        next_node = curr_left
      else:
        next_node = curr_right
      if self.storage[index] <= self.storage[next_node]:
        temp = self.storage[index]
        self.storage[index] = self.storage[next_node]
        self.storage[next_node] = temp
      index = next_node

