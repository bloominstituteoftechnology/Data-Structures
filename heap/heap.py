class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    index = len(self.storage) - 1
    self.storage.append(value)
    self._bubble_up(index)
    
  def delete(self):
    element = self.storage.pop(0)
    self._sift_down(0)
    return element

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    left_child = (2*index) + 1
    right_child = (2*index) + 2
    print(self.storage)
    print(self.storage[left_child], self.storage[right_child])
    print(len(self.storage))
    # if left_child > self.get_size() or right_child > self.get_size():
    if self.storage[left_child] < self.storage[right_child]:
      child = right_child
    else:
      child = left_child
    print(self.storage[child], self.storage[index])
    if self.storage[child] > self.storage[index]:
      self.storage[child], self.storage[index] = self.storage[index], self.storage[child]
      return self._sift_down(child)

