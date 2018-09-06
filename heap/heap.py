class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.get_size() - 1)

  def delete(self):
    value = self.storage[0]
    self.storage[0] = self.storage[self.get_size() - 1]
    self._sift_down(0)
    self.storage.pop()
    return value

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_i = (index - 1) // 2
    while self.storage[index] > self.storage[parent_i]:
      self.storage[parent_i], self.storage[index] = self.storage[index], self.storage[parent_i]
      parent_i = parent_i // 2

  def _sift_down(self, index):
    while index * 2 <= self.get_size():
      left_i = 2 * index + 1
      right_i = left_i + 1
      if self.storage[index] < self.storage[right_i]:
        self.storage[index], self.storage[right_i] = self.storage[right_i], self.storage[index]
        index = right_i
      elif self.storage[index] < self.storage[left_i]:
        self.storage[index], self.storage[left_i] = self.storage[left_i], self.storage[index]
        index = left_i
      