class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    if len(self.storage) == 1:
      return self.storage.pop()

    max_el = self.get_max()
    self.storage[0] = self.storage.pop()
    self._sift_down(0)
    return max_el

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _get_parent_index(self, index):
    return (index - 1) // 2

  def _get_left_index(self, index):
    left_index = index * 2 + 1
    return left_index if not left_index > len(self.storage) else None

  def _get_right_index(self, index):
    right_index = index * 2 + 2
    return right_index if not right_index > len(self.storage) else None

  def _element_at(self, index):
    if index is None or index > len(self.storage) - 1:
      return None

    return self.storage[index]

  def _bubble_up(self, index):
    el = self._element_at(index)
    parent_index = self._get_parent_index(index)
    parent = self._element_at(parent_index)
    if parent is None or parent > el or parent_index < 0:
      return
    else:
      self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    left_index = self._get_left_index(index)
    right_index = self._get_right_index(index)
    curr_el = self._element_at(index)
    left_el = self._element_at(left_index)
    right_el = self._element_at(right_index)

    if left_el is not None:
      if left_el > curr_el:
        self.storage[index], self.storage[left_index] = self.storage[left_index], self.storage[index]
        self._sift_down(left_index)
    if right_el is not None:
      if right_el > curr_el:
        self.storage[index], self.storage[right_index] = self.storage[right_index], self.storage[index]
        self._sift_down(right_index)

# class Heap:
#   def __init__(self):
#     self.storage = []
#     self.count = 0
#
#   def insert(self, value):
#     self.storage.append(value)
#     self.count += 1
#     parent = self._get_parent_index(self.count - 1)
#     while parent < value:
#       curr_index = self._bubble_up(self.count - 1)
#       parent = self._get_parent_index(curr_index)
#
#   def delete(self):
#     pass
#
#   def get_max(self):
#     pass
#
#   def get_size(self):
#     return self.count
#
#   def _get_parent_index(self, index):
#     return (index - 1) // 2
#
#   def _get_left(self, index):
#     left_index = index * 2 + 1
#     if left_index > self.count -1:
#       return None
#     else:
#       return left_index
#
#   def _get_left(self, index):
#     right_index = index * 2 + 2
#     if right_index > self.count -1:
#       return None
#     else:
#       return right_index
#
#   def _bubble_up(self, index):
#     pass
#
#   def _sift_down(self, index):
#     pass
