from math import floor

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):

    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)


  def delete(self):
    deleted = self.storage[1]
    last = self.storage[self.size]
    self.storage[1] = last
    self.storage.pop()
    self.size -= 1
    self._sift_down(1)
    return deleted

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    child = self.storage[index]
    parent = self.storage[floor(index / 2)]
    if index == 1:
      return None

    elif self.storage[floor(index / 2)] == 0:
      return None

    elif self.storage[index] > self.storage[floor(index / 2)]:
      tmp_child = self.storage[index]
      tmp_parent = self.storage[floor(index / 2)]
      self.storage[floor(index / 2)] = tmp_child
      self.storage[index] = tmp_parent
      return self._bubble_up(floor(index / 2))

    else:
      None  

  def _sift_down(self, index):
    if 2 * index < self.size or 2 * index + 1 < self.size:
      if (self.storage[index] < self.storage[2 * index]) or (self.storage[index] < self.storage[2 * index + 1]):
        
        tmp_parent = self.storage[index]

        if self.storage[2 * index] < self.storage[2 * index + 1]:
          tmp_child = self.storage[2 * index + 1]
          self.storage[2 * index + 1] = tmp_parent
          self.storage[index] = tmp_child
          if 2 * index + 1 < self.size:
            return self._sift_down(2 * index + 1)
          else:
            return None

        else:
          tmp_child = self.storage[2 * index]
          self.storage[2 * index] = tmp_parent
          self.storage[index] = tmp_child
          if 2 * index < self.size:
            return self._sift_down(2 * index)
          else:
            return None

    else:
      None
