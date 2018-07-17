class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    if self.size == 0:
      return None
    elif self.size == 1:
      self.size -= 1
      return self.storage.pop()
    else:
      new_node = self.storage.pop()
      old_node = self.storage[1]
      self.storage[1]= new_node
      self.size -= 1
      self._sift_down(1)
      return old_node

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    parent_index = index // 2

    if parent_index >= 1 and self.storage[index] > self.storage[parent_index]:
      container = self.storage[index]
      self.storage[index] = self.storage[parent_index]
      self.storage[parent_index] = container
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    left = 2 * (index + 1)
    right = 2 * (index + 2)

    if self.size == 2:
      if self.storage[1] < self.storage[2]:
        container = self.storage[1]
        self.storage[1] = self.storage[2]
        self.storage[2] = container

    if left > self.size - 1 and right > self.size - 1:
      return
    tail = self.storage[index]

    if tail < self.storage[left] and self.storage[right] >= self.storage[left]:
      container = tail
      self.storage[index] = self.storage[right]
      self.storage[right] = container
      self._sift_down(right)
    elif tail < self.storage[left] and self.storage[right] < self.storage[left]:
      container = tail
      self.storage[index] = self.storage[left]
      self.storage[left] = container
      self._sift_down(left)

    if right > self.size and tail < self.storage[left]:
      container = tail
      self.storage[index] = self.storage[left]
      self.storage[left] = container
      self._sift_down(left)