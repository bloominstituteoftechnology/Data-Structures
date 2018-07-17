class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    # self.storage = [0, 1, 2, 3]
    # self.size = 3
    if self.size > 0:
      self.size += 1
      self.storage.append(value)
      self._bubble_up(self.size)

    else:
      self.size += 1
      self.storage.append(value)
      self._bubble_up(self.size)

  def delete(self):
    if self.size > 0:
      maxval = self.get_max()
      self.storage[1] = self.storage[self.size]
      del self.storage[-1]
      self.size -= 1
      self._sift_down(1)

      return maxval


  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    parent_index = index // 2
    if parent_index == 0:
      pass
    else:
      child = self.storage[index]
      parent = self.storage[parent_index]
      if child > parent:
        temp = child
        # why doesn't this work? --> child, parent = parent, child
        self.storage[index] = self.storage[parent_index]
        self.storage[parent_index] = temp
        self._bubble_up(parent_index)

  def _sift_down(self, index):
    left_child_index = 2 * index
    right_child_index = 2 * index + 1
    if right_child_index > self.size:
      if left_child_index > self.size:
        return 'done'
      else:
        left_child = self.storage[left_child_index]
        parent = self.storage[index]
        if left_child > parent:
          temp = left_child
          self.storage[left_child_index] = self.storage[index]
          self.storage[index] = temp
          self._sift_down(left_child_index)
        else:
          return 'done'

    else:
      left_child = self.storage[left_child_index]
      right_child = self.storage[right_child_index]
      larger_child = left_child if left_child > right_child else right_child
      larger_child_index = left_child_index if left_child > right_child else right_child_index
      parent = self.storage[index]

      if larger_child > parent:
        temp = larger_child
        self.storage[larger_child_index] = self.storage[index]
        self.storage[index] = temp
        self._sift_down(larger_child_index)
      else:
        return 'done'
