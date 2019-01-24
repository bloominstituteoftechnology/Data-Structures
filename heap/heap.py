import math
class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage)-1
    if len(self.storage) >= 2:
      self._bubble_up(index)

  def delete(self):
    size = len(self.storage)
    top = self.storage[0]
    self.storage[0] = self.storage[size-1] 
    self._sift_down(0)
    return top

  def get_max(self):
    if len(self.storage) > 0:
      return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_index = self._get_parent_index(index)
    while self.storage[parent_index] < self.storage[index]:
        print(f'{self.storage[index]} is greater than {self.storage[parent_index]}. lets swap them')
        self._swap(index, parent_index)
        # It is only swapping ONE time with parent ????????
        index = parent_index



  def _sift_down(self, index):
    left_child_index = self._get_left_child_index(index)
    right_child_index = self._get_right_child_index(index)
    
    if left_child_index:
      if self.storage[left_child_index] > self.storage[right_child_index]:
        self._swap(left_child_index, index)
      else:
        self._swap(right_child_index, index)
  def _get_parent_index(self, index):
    return math.floor((index - 1) / 2)
  def _get_left_child_index(self, index):
    return (index * 2) + 1
  def _get_right_child_index(self, index):
    return (index * 2) + 2
  
  def _swap(self, index, parent_index):
    tmp = self.storage[index]
    self.storage[index] = self.storage[parent_index]
    self.storage[parent_index] = tmp



# heap = Heap()
# heap.insert(6)
# heap.insert(8)
# heap.insert(10)