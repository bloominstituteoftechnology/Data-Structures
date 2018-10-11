import math
class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    heap = self.storage
    heap.append(value)
    parent = math.floor((heap.index(value)-1)/2)
    while heap[parent] < value:
      return self._bubble_up(parent)

  def delete(self):
    heap = self.storage
    toDelete = heap[0]
    if len(heap) > 1:
      heap[0] = heap[-1]
      del heap[-1]
      if len(heap) == 1:
        return toDelete
      elif len(heap) == 2:
        if heap[0] < heap[1]:
          replace = heap[0]
          heap[0] = heap[1]
          heap[1] = replace
      elif heap[0] < heap[1] or heap[0] < heap[2]:
        self._sift_down(0)
    else:
      heap = []
    return toDelete

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    heap = self.storage
    oldParent = heap[index]
    if (2 * index) + 2 > heap.index(heap[-1]):
      heap[index] = heap[(2 * index) + 1]
      heap[(2 * index) + 1] = oldParent
    elif heap[(2 * index) + 1] > heap[(2 * index) + 2]:
      heap[index] = heap[(2 * index) + 1]
      heap[(2 * index) + 1] = oldParent
    else:
      heap[index] = heap[(2 * index) + 2]
      heap[(2 * index) + 2] = oldParent 

  def _sift_down(self, index):
    heap = self.storage
    oldParent = heap[index]
    if heap[(2 * index) + 2] == IndexError:
      heap[index] = heap[(2 * index) + 1]
      heap[(2 * index) + 1] = oldParent
    elif heap[(2 * index) + 1] > heap[(2 * index) + 2]:
      heap[index] = heap[(2 * index) + 1]
      heap[(2 * index) + 1] = oldParent
      newindex = (2 * index) + 1
      if (2 * newindex) + 1 < len(heap) and heap[(2 * newindex) + 1] > heap[newindex] or (2 * newindex) + 2 < len(heap) and heap[(2 * newindex) + 2] > heap[newindex]:
        return self._sift_down(newindex)
    elif heap[(2 * index) + 1] < heap[(2 * index) + 2]:
      heap[index] = heap[(2 * index) + 2]
      heap[(2 * index) + 2] = oldParent
      newindex = (2 * index) + 2
      if (2 * newindex) + 1 < len(heap) and heap[(2 * newindex) + 1] > heap[newindex] or (2 * newindex) + 2 < len(heap) and heap[(2 * newindex) + 2] > heap[newindex]:
        return self._sift_down(newindex)
