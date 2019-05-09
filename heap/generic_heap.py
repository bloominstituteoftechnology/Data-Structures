class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) -1)
  

  def delete(self):
    if len(self.storage) == 0:
      return False
    item = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self._sift_down(0)

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index == 0:
      return
    parent_index = ((index + 1) // 2) -1
    if self.storage[index] > self.storage[parent_index]:
      self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
    return self._bubble_up(parent_index)

  def _sift_down(self, index):
    left_child = 2 * index + 1
    while left_child < len(self.storage)

heap = Heap(None)
heap.insert(6)
heap.insert(8)
heap.insert(10)
heap.insert(9)
heap.insert(1)
heap.insert(9)
heap.insert(9)
heap.insert(5) 

print(heap.storage)