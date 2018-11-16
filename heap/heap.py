import math 

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage)-1
    parent = self.parent(index)
    while index and self.storage[index] > self.storage[parent]:
      self._bubble_up(index, parent)
      index = parent
      parent = self.parent(index)

  def delete(self):
    self.storage[0] = self.storage.pop() if len(self.storage) > 1 else self.storage.append(self.storage.pop())
    index = 0
    left_child = self.left_child(index)
    right_child = self.right_child(index)

    while left_child <= (len(self.storage)-1 ):
      print ('Left, Index, Len Storage:', left_child, index, len(self.storage))
      print (self.storage)
      if right_child <= len(self.storage)-1:
        if self.storage[index] < self.storage[right_child] or self.storage[index] < self.storage[left_child]:
          larger_child = left_child if self.storage[left_child] > self.storage[right_child] else right_child
          self._sift_down(index, larger_child)
          index = larger_child
          left_child = self.left_child(index)
          right_child = self.right_child(index)
      elif self.storage[index] < self.storage[left_child]:
        print ('lefty running')
        self._sift_down(index, left_child)
        index = left_child
        left_child = self.left_child(index)
        right_child = self.right_child(index)
      else:
        break
      print ('ignorando todo putos')

        #todavia no has comparado si el child es mas pequeño/grande que el current index
        #asigná el nuevo parent y children (como en lines 38-40)

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index, parent):
    hold = self.storage[parent]
    self.storage[parent] = self.storage[index]
    self.storage[index] = hold

  def _sift_down(self, index, larger_child):
    print ('Index, Larger:', index, larger_child)
    hold = self.storage[larger_child]
    self.storage[larger_child] = self.storage[index]
    self.storage[index] = hold


  def parent(self, index):
   return int(math.floor((index-1)/2)) if index else None

  def left_child(self, index):
    return (index*2)+1

  def right_child(self, index):
    return (index*2)+2