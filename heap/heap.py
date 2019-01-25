class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.get_size() - 1)

  def delete(self):
    self.storage[:1], self.storage[-1:] = self.storage[-1:], self.storage[:1]
    to_delete = self.storage.pop()
    self._sift_down(0)
    return to_delete

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _swap(self, idx1, idx2):
    self.storage[idx1], self.storage[idx2] = self.storage[idx2], self.storage[idx1]

  def _get_parent(self, index):
    return self.storage[(index - 1) // 2]
  
  def _get_right_child(self, index):
    r = index * 2 + 2
    return self.storage[r]
  
  def _get_left_child(self, index):
    l = index * 2 + 1
    return self.storage[l]

  def _get_max_child_index(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      right_child = self._get_right_child(index)
      left_child = self._get_left_child(index)
      return (index * 2) + 2 if right_child > left_child else (index * 2) + 1

  def _bubble_up(self, index):
    # 1. While we're not at the top
    # If the current element is greater than it's parent, swap them
    # Set the new index to the parents index (since they've swapped)
    while (index - 1) // 2 >= 0:
      if self.storage[index] > self.storage[(index - 1) // 2]:
        self._swap(index, (index - 1) // 2)
      index = (index - 1) // 2
      
  def _sift_down(self, index):
    # 1. While left index is less than the last element in our heap
    # 2. Get the max child of this element
    # 3. If the current element is less than the max child, swap them
    # 4. Set the new index to the max child index since they have swapped
    while index * 2 + 1 <= self.get_size() - 1:
      max_child_index = self._get_max_child_index(index)
      if self.storage[index] < self.storage[max_child_index]:
        self._swap(index, max_child_index)
      index = max_child_index