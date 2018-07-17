import math

class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    index = 0 if self.get_size() == 0 else self.get_size() - 1
    self._bubble_up(index)

  def delete(self):
    # swap root with last node
    root = self.storage[0]
    self.storage[0] = self.storage[self.get_size() - 1]
    self.storage[self.get_size() - 1] = root

    # pop off last node
    max = self.storage.pop(self.get_size() - 1)

    # sift down
    if self.get_size() > 1:
        index = 0
        while index:
            index = self._sift_down(index)
            
    return max

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_index = math.floor((index-1)/2)

    while self.storage[parent_index] < self.storage[index]:
        parent = self.storage[parent_index]
        self.storage[parent_index] = self.storage[index]
        self.storage[index] = parent
        parent_index = math.floor((parent_index-1)/2)

  def _sift_down(self, index):
    left_child_index = (2*index) + 1
    left_child = self.storage[left_child_index]
    right_child_index = (2*index) + 2
    right_child = self.storage[right_child_index]
    parent = self.storage[index]

    if left_child > parent and left_child > right_child:
        self.storage[left_child_index] = parent
        self.storage[index] = left_child
        return left_child_index
    elif right_child > parent and right_child > left_child:
        self.storage[right_child_index] = parent
        self.storage[index] = right_child
        return right_child_index
    
    return None
