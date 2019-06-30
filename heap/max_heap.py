class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    removed = self.storage[0]
    del self.storage[0]
    self._sift_down(0)
    return removed

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent = (index - 1) // 2
    while parent >= 0:
      if self.storage[parent] < self.storage[index]:
        self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
      parent = (parent - 1) // 2

  def _sift_down(self, index):
    parent_index = index
    left_child = parent_index * 2 + 1
    right_child = parent_index * 2 + 2

    #while index is smaller than storage length
    while left_child <= len(self.storage) - 1:
      #if right child is valid
      if (right_child > len(self.storage) - 1) or (self.storage[left_child] > self.storage[right_child]):
        maxIndex = left_child
      else:
        maxIndex = right_child

      #check to see if left and right exist
      if self.storage[maxIndex] > self.storage[index]:
        self.storage[maxIndex], self.storage[index] = self.storage[index], self.storage[maxIndex]
      index = maxIndex
      left_child = maxIndex * 2 + 1
      right_child = maxIndex * 2 + 2

heap = Heap()
heap.insert(6)
heap.insert(7)
heap.insert(5)
heap.insert(8)
heap.insert(10)
heap.insert(1)
heap.insert(2)
heap.insert(5)

print(heap)