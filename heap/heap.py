class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    max = self.storage[1] #store max so we can return it
    #replace first storage el w last el in the heap
    if len(self.storage) == 1:
      return None
    
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    self.storage.pop()
    self._sift_down(1)
    return max

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index // 2] < self.storage[index]:
        self.storage[index // 2], self.storage[index] = self.storage[index], self.storage[index // 2]
      else:
        break
      index = index / 2

  def _sift_down(self, index):
    while (index * 2) <= self.size:
      maxChild = self._max_child(index)
      if self.storage[index] < self.storage[maxChild]:
        self.storage[index], self.storage[maxChild] = self.storage[maxChild], self.storage[index]
      else:
        break
      index = maxChild
  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1
