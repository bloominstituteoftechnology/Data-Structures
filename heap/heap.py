class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    first = self.storage.pop(0)
    self.storage = self.storage[-1:] + self.storage[:-1]
    self._sift_down(0)
    return first

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_index = (index - 1) // 2
    if index <= 0:
      return True
    elif self.storage[parent_index] < self.storage[index]:
      self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    # leftchild = index * 2 + 1
    # rightchild = index * 2 + 2
    # newindex = index

    # if leftchild <= len(self.storage) - 1:
    #   left_child_val = self.storage[leftchild]
    #   if left_child_val > self.storage[newindex]:
    #     newindex = leftchild
    # if rightchild <= len(self.storage) - 1:
    #   right_child_val = self.storage[rightchild]
    #   if right_child_val > self.storage[newindex]:
    #     newindex = rightchild
    # if newindex is not index:
    #   self.storage[index], self.storage[newindex] = self.storage[newindex], self.storage[index]
    #   self._sift_down(newindex)
   
    first_child = (2 * index) + 1
    second_child = first_child + 1
    if first_child > len(self.storage) - 1:
      return True
    elif first_child <= len(self.storage) - 1 and second_child <= len(self.storage) - 1:
      swap_index = self.storage.index(max(self.storage[first_child], self.storage[second_child]))
      if self.storage[swap_index] > self.storage[index]:
        self.storage[index], self.storage[swap_index] = self.storage[swap_index], self.storage[index]
        self._sift_down(swap_index)
    elif self.storage[first_child] > self.storage[index]:
      self.storage[index], self.storage[first_child] = self.storage[first_child], self.storage[index]
      self._sift_down(first_child)
