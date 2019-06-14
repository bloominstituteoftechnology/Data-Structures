class Heap:
  def __init__(self):
    self.storage = []
    self.currentSize = 0
    # self.comparator = comparator

  def insert(self, value):
    if self.currentSize == 0:
      self.storage = [value]
      self.currentSize += 1
    else:
      self.storage.append(value)
      self._bubble_up(self.currentSize)
      self.currentSize += 1

  def delete(self):
    pass

  def get_priority(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    while index > 0:
      parent = (index-1) // 2
      if self.storage[index] > self.storage[parent]:
        store = self.storage[parent]
        self.storage[parent] = self.storage[index]
        self.storage[index] = store
        index = parent
      else:
        break

  def _sift_down(self, index):
    pass


heap = Heap()

heap.insert(6)
heap.insert(8)
heap.insert(10)
heap.insert(2)
print(heap.storage)