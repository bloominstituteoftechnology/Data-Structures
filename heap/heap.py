class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # Add to end of heap, then compare to parents until correct order
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)


  def delete(self):
    # Store the first element as rv, then put last element in first spot. Commpare with children until correct order
    rv = self.storage.pop(0)
    self._sift_down(0)
    return rv


  def get_max(self):
    # Return first element in heap
    return self.storage[0]

  def get_size(self):
    # Return length of heap storage
    return len(self.storage)

  def _bubble_up(self, index):
    # Compare element with it's parent. If element is larger, then swap with parent
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    # Compare element's children. If one is larger, then swap. If both are larger, then take the larger one and swap.
    while index * 2 + 1 <= len(self.storage) - 1:
        max_child = self._max_child(index)
        if self.storage[index] < self.storage[max_child]:
            self.storage[index], self.storage[max_child] = self.storage[max_child], self.storage[index]
        index = max_child

  def _max_child(self, index):
      if index * 2 + 2 > len(self.storage) - 1:
          return index * 2 + 1
      else:
          return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2
