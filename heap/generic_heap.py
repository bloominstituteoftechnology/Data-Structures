class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
      index = self.size()
      self.storage.append(value)

  def delete(self):
    pass

  def get_priority(self):
    pass

  def get_size(self):
      return len(self.storage)

  def _bubble_up(self, index):
      while index > 0:
          # compare to parent
          parent = (index - 1) // 2

          if self.storage[index] > self.storage[parent]:
              self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

              index = parent
          else:
              break

  def _sift_down(self, index):
    pass
