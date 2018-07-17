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
    top = self.storage[1]
    last = self.storage.pop()
    self.size -= 1
    if self.size == 0:
      return top

    self.storage[1] = last
    self._sift_down(1)
    return top

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def swap(self, index1, index2):
    val1 = self.storage[index1]
    self.storage[index1] = self.storage[index2]
    self.storage[index2] = val1

  def _bubble_up(self, index):
    parent_index = index//2
    if parent_index == 0:
      return

    if self.storage[parent_index] < self.storage[index]:
      self.swap(parent_index, index)
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    left_index = index if 2*index > self.size else 2*index
    right_index = index if 2*index+1 > self.size else 2*index+1
    child_index = left_index if self.storage[left_index] > self.storage[right_index] else right_index
    if child_index == index:
      return

    if self.storage[child_index] > self.storage[index]:
      self.swap(index, child_index)
      self._sift_down(child_index)