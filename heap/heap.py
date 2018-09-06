class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    rv = self.storage[1]
    self.storage[1] = self.storage[len(self.storage)-1]
    self.storage.pop()
    self._sift_down(1)
    return rv

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index // 2 > 0 and index <= len(self.storage):
      if self.storage[index] < self.storage[(index+1) // 2]:
        tmp = self.storage[(index+1) // 2]
        self.storage[(index+1) // 2] = self.storage[index]
        self.storage[index] = tmp
      index = (index+1) // 2

  def get_min(self, index):
    #find minchild
    if index * 2 + 1 > len(self.storage):
      return index * 2
    else:
      if self.storage[index * 2] < self.storage[index * 2 + 1]:
        return index * 2
      else:
        return index * 2 + 1

  def _sift_down(self, index):
    while (i * 2) <= len(self.storage):
      mc = self.get_min(i)
      if self.storage[index] > self.storage[mc]:
        tmp = self.storage[index]
        self.storage[i] = self.storage[mc]
        self.storage[mc] = tmp
      i = mc
